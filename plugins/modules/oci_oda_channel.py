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
module: oci_oda_channel
short_description: Manage a Channel resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Channel resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Channel.
    - "This resource has the following action operations in the M(oracle.oci.oci_oda_channel_actions) module: rotate_channel_keys, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    host:
        description:
            - The host.
            - For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface
              or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch,
              then the host is sitename.exampledomain.com.
            - "For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL.
              For example: sitename.exampledomain.com."
            - This parameter is updatable.
            - Applicable when type is 'OSVC'
            - Required when type is 'OSVC'
        type: str
    port:
        description:
            - The port.
            - This parameter is updatable.
            - Applicable when type is 'OSVC'
            - Required when type is 'OSVC'
        type: str
    total_session_count:
        description:
            - The total session count.
            - This parameter is updatable.
            - Applicable when type is 'OSVC'
            - Required when type is 'OSVC'
        type: int
    channel_service:
        description:
            - The type of OSVC service.
            - This parameter is updatable.
            - Applicable when type is 'OSVC'
        type: str
        choices:
            - "OSVC"
            - "FUSION"
    authentication_provider_name:
        description:
            - The name of the Authentication Provider to use to authenticate the user.
            - This parameter is updatable.
            - Applicable when type is 'OSVC'
            - Required when type is 'OSVC'
        type: str
    inbound_message_topic:
        description:
            - The topic inbound messages are received on.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    outbound_message_topic:
        description:
            - The topic outbound messages are sent on.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    bootstrap_servers:
        description:
            - The Oracle Streaming Service bootstrap servers.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    security_protocol:
        description:
            - The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid
              values.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    sasl_mechanism:
        description:
            - The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    tenancy_name:
        description:
            - The tenancy to use when connecting to the Oracle Streaming Service.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    stream_pool_id:
        description:
            - The stream pool OCI to use when connecting to the Oracle Streaming Service.
            - This parameter is updatable.
            - Applicable when type is 'OSS'
            - Required when type is 'OSS'
        type: str
    event_sink_bot_ids:
        description:
            - The IDs of the Skills and Digital Assistants that the Channel is routed to.
            - This parameter is updatable.
            - Applicable when type is one of ['APPEVENT', 'OSS']
        type: list
        elements: str
    allowed_domains:
        description:
            - A comma-delimited whitelist of allowed domains.
            - "The channel will only communicate with the sites from the domains that you add to this list.
              For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access
              to the channel from any domain."
            - Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.
            - This parameter is updatable.
            - Applicable when type is 'WEB'
        type: str
    max_token_expiration_time_in_minutes:
        description:
            - The maximum time until the token expires (in minutes).
            - This parameter is updatable.
            - Applicable when type is one of ['WEB', 'ANDROID', 'IOS']
        type: int
    is_client_authentication_enabled:
        description:
            - Whether client authentication is enabled or not.
            - This parameter is updatable.
            - Applicable when type is one of ['WEB', 'ANDROID', 'IOS']
            - Required when type is one of ['WEB', 'ANDROID', 'IOS']
        type: bool
    client_id:
        description:
            - The Slack Client Id for the Slack app.
            - This parameter is updatable.
            - Applicable when type is 'SLACK'
            - Required when type is 'SLACK'
        type: str
    auth_success_url:
        description:
            - The URL to redirect to when authentication is successful.
            - This parameter is updatable.
            - Applicable when type is 'SLACK'
        type: str
    auth_error_url:
        description:
            - The URL to redirect to when authentication is unsuccessful.
            - This parameter is updatable.
            - Applicable when type is 'SLACK'
        type: str
    signing_secret:
        description:
            - The Signing Secret for the Slack App.
            - This parameter is updatable.
            - Applicable when type is 'SLACK'
            - Required when type is 'SLACK'
        type: str
    client_secret:
        description:
            - The Client Secret for the Slack App.
            - This parameter is updatable.
            - Applicable when type is 'SLACK'
            - Required when type is 'SLACK'
        type: str
    domain_name:
        description:
            - The domain name.
            - If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
              Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
              is sitename and the domain name is exampledomain.com.
            - If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
              then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like
              sitename-2.exampledomain.com.
            - This parameter is updatable.
            - Applicable when type is 'SERVICECLOUD'
            - Required when type is 'SERVICECLOUD'
        type: str
    host_name_prefix:
        description:
            - The host prefix.
            - If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the
              Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix
              is sitename and the domain name is exampledomain.com.
            - If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces,
              then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like
              sitename-2.exampledomain.com.
            - This parameter is updatable.
            - Applicable when type is 'SERVICECLOUD'
            - Required when type is 'SERVICECLOUD'
        type: str
    user_name:
        description:
            - The user name for an Oracle B2C Service staff member who has the necessary profile permissions.
            - This parameter is updatable.
            - Applicable when type is one of ['OSVC', 'SERVICECLOUD', 'OSS']
            - Required when type is one of ['OSVC', 'SERVICECLOUD', 'OSS']
        type: str
    password:
        description:
            - The password for the Oracle B2C Service staff member who has the necessary profile permissions.
            - This parameter is updatable.
            - Applicable when type is one of ['OSVC', 'SERVICECLOUD']
            - Required when type is one of ['OSVC', 'SERVICECLOUD']
        type: str
    client_type:
        description:
            - The type of Service Cloud client.
            - This parameter is updatable.
            - Applicable when type is 'SERVICECLOUD'
            - Required when type is 'SERVICECLOUD'
        type: str
        choices:
            - "WSDL"
            - "REST"
    account_sid:
        description:
            - The Account SID for the Twilio number.
            - This parameter is updatable.
            - Applicable when type is 'TWILIO'
            - Required when type is 'TWILIO'
        type: str
    phone_number:
        description:
            - The Twilio phone number.
            - This parameter is updatable.
            - Applicable when type is 'TWILIO'
            - Required when type is 'TWILIO'
        type: str
    auth_token:
        description:
            - The authentication token to use when connecting to the Oracle Streaming Service.
            - This parameter is updatable.
            - Applicable when type is one of ['OSS', 'TWILIO']
            - Required when type is one of ['OSS', 'TWILIO']
        type: str
    is_mms_enabled:
        description:
            - Whether MMS is enabled for this channel or not.
            - This parameter is updatable.
            - Applicable when type is 'TWILIO'
            - Required when type is 'TWILIO'
        type: bool
    original_connectors_url:
        description:
            - The original connectors URL (used for backward compatibility).
            - This parameter is updatable.
            - Applicable when type is 'TWILIO'
        type: str
    payload_version:
        description:
            - The version for payloads.
            - This parameter is updatable.
            - Applicable when type is 'WEBHOOK'
            - Required when type is 'WEBHOOK'
        type: str
        choices:
            - "1.0"
            - "1.1"
    outbound_url:
        description:
            - The URL to send response and error messages to.
            - This parameter is updatable.
            - Applicable when type is one of ['APPLICATION', 'WEBHOOK', 'APPEVENT']
            - Required when type is 'WEBHOOK'
        type: str
    is_authenticated_user_id:
        description:
            - True if the user id in the AIC message should be treated as an authenticated user id.
            - This parameter is updatable.
            - Applicable when type is 'APPLICATION'
            - Required when type is 'APPLICATION'
        type: bool
    app_secret:
        description:
            - The app secret for your Facebook app.
            - This parameter is updatable.
            - Applicable when type is 'FACEBOOK'
            - Required when type is 'FACEBOOK'
        type: str
    page_access_token:
        description:
            - The page access token that you generated for your Facebook page.
            - This parameter is updatable.
            - Applicable when type is 'FACEBOOK'
            - Required when type is 'FACEBOOK'
        type: str
    description:
        description:
            - A short description of the Channel.
            - This parameter is updatable.
        type: str
    type:
        description:
            - The Channel type.
            - Required for create using I(state=present), update using I(state=present) with channel_id present.
        type: str
        choices:
            - "MSTEAMS"
            - "WEB"
            - "FACEBOOK"
            - "APPLICATION"
            - "SERVICECLOUD"
            - "SLACK"
            - "OSVC"
            - "APPEVENT"
            - "OSS"
            - "CORTANA"
            - "ANDROID"
            - "TWILIO"
            - "WEBHOOK"
            - "IOS"
    session_expiry_duration_in_milliseconds:
        description:
            - The number of milliseconds before a session expires.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    msa_app_id:
        description:
            - The Microsoft App ID that you obtained when you created your bot registration in Azure.
            - This parameter is updatable.
            - Applicable when type is one of ['MSTEAMS', 'CORTANA']
            - Required when type is one of ['MSTEAMS', 'CORTANA']
        type: str
    msa_app_password:
        description:
            - The client secret that you obtained from your bot registration.
            - This parameter is updatable.
            - Applicable when type is one of ['MSTEAMS', 'CORTANA']
            - Required when type is one of ['MSTEAMS', 'CORTANA']
        type: str
    bot_id:
        description:
            - The ID of the Skill or Digital Assistant that the Channel is routed to.
            - This parameter is updatable.
            - Applicable when type is one of ['FACEBOOK', 'MSTEAMS', 'OSVC', 'WEB', 'SLACK', 'WEBHOOK', 'ANDROID', 'IOS', 'CORTANA', 'TWILIO']
        type: str
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    channel_id:
        description:
            - Unique Channel identifier.
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
- name: Create channel with type = MSTEAMS
  oci_oda_channel:
    # required
    name: name_example
    type: MSTEAMS

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = WEB
  oci_oda_channel:
    # required
    name: name_example
    type: WEB

    # optional
    allowed_domains: allowed_domains_example
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = FACEBOOK
  oci_oda_channel:
    # required
    name: name_example
    type: FACEBOOK

    # optional
    app_secret: app_secret_example
    page_access_token: page_access_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = APPLICATION
  oci_oda_channel:
    # required
    name: name_example
    type: APPLICATION

    # optional
    outbound_url: outbound_url_example
    is_authenticated_user_id: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create channel with type = SERVICECLOUD
  oci_oda_channel:
    # required
    name: name_example
    type: SERVICECLOUD

    # optional
    domain_name: domain_name_example
    host_name_prefix: host_name_prefix_example
    user_name: user_name_example
    password: example-password
    client_type: WSDL
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create channel with type = SLACK
  oci_oda_channel:
    # required
    name: name_example
    type: SLACK

    # optional
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    auth_success_url: auth_success_url_example
    auth_error_url: auth_error_url_example
    signing_secret: signing_secret_example
    client_secret: client_secret_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = OSVC
  oci_oda_channel:
    # required
    name: name_example
    type: OSVC

    # optional
    host: host_example
    port: port_example
    total_session_count: 56
    channel_service: OSVC
    authentication_provider_name: authentication_provider_name_example
    user_name: user_name_example
    password: example-password
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = APPEVENT
  oci_oda_channel:
    # required
    name: name_example
    type: APPEVENT

    # optional
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create channel with type = OSS
  oci_oda_channel:
    # required
    name: name_example
    type: OSS

    # optional
    inbound_message_topic: inbound_message_topic_example
    outbound_message_topic: outbound_message_topic_example
    bootstrap_servers: bootstrap_servers_example
    security_protocol: security_protocol_example
    sasl_mechanism: sasl_mechanism_example
    tenancy_name: tenancy_name_example
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    user_name: user_name_example
    auth_token: auth_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create channel with type = CORTANA
  oci_oda_channel:
    # required
    name: name_example
    type: CORTANA

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = ANDROID
  oci_oda_channel:
    # required
    name: name_example
    type: ANDROID

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = TWILIO
  oci_oda_channel:
    # required
    name: name_example
    type: TWILIO

    # optional
    account_sid: account_sid_example
    phone_number: phone_number_example
    auth_token: auth_token_example
    is_mms_enabled: true
    original_connectors_url: original_connectors_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = WEBHOOK
  oci_oda_channel:
    # required
    name: name_example
    type: WEBHOOK

    # optional
    payload_version: 1.0
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create channel with type = IOS
  oci_oda_channel:
    # required
    name: name_example
    type: IOS

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = MSTEAMS
  oci_oda_channel:
    # required
    type: MSTEAMS

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = WEB
  oci_oda_channel:
    # required
    type: WEB

    # optional
    allowed_domains: allowed_domains_example
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = FACEBOOK
  oci_oda_channel:
    # required
    type: FACEBOOK

    # optional
    app_secret: app_secret_example
    page_access_token: page_access_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = APPLICATION
  oci_oda_channel:
    # required
    type: APPLICATION

    # optional
    outbound_url: outbound_url_example
    is_authenticated_user_id: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel with type = SERVICECLOUD
  oci_oda_channel:
    # required
    type: SERVICECLOUD

    # optional
    domain_name: domain_name_example
    host_name_prefix: host_name_prefix_example
    user_name: user_name_example
    password: example-password
    client_type: WSDL
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel with type = SLACK
  oci_oda_channel:
    # required
    type: SLACK

    # optional
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    auth_success_url: auth_success_url_example
    auth_error_url: auth_error_url_example
    signing_secret: signing_secret_example
    client_secret: client_secret_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = OSVC
  oci_oda_channel:
    # required
    type: OSVC

    # optional
    host: host_example
    port: port_example
    total_session_count: 56
    channel_service: OSVC
    authentication_provider_name: authentication_provider_name_example
    user_name: user_name_example
    password: example-password
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = APPEVENT
  oci_oda_channel:
    # required
    type: APPEVENT

    # optional
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel with type = OSS
  oci_oda_channel:
    # required
    type: OSS

    # optional
    inbound_message_topic: inbound_message_topic_example
    outbound_message_topic: outbound_message_topic_example
    bootstrap_servers: bootstrap_servers_example
    security_protocol: security_protocol_example
    sasl_mechanism: sasl_mechanism_example
    tenancy_name: tenancy_name_example
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    user_name: user_name_example
    auth_token: auth_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel with type = CORTANA
  oci_oda_channel:
    # required
    type: CORTANA

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = ANDROID
  oci_oda_channel:
    # required
    type: ANDROID

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = TWILIO
  oci_oda_channel:
    # required
    type: TWILIO

    # optional
    account_sid: account_sid_example
    phone_number: phone_number_example
    auth_token: auth_token_example
    is_mms_enabled: true
    original_connectors_url: original_connectors_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = WEBHOOK
  oci_oda_channel:
    # required
    type: WEBHOOK

    # optional
    payload_version: 1.0
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel with type = IOS
  oci_oda_channel:
    # required
    type: IOS

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = MSTEAMS
  oci_oda_channel:
    # required
    name: name_example
    type: MSTEAMS

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = WEB
  oci_oda_channel:
    # required
    name: name_example
    type: WEB

    # optional
    allowed_domains: allowed_domains_example
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = FACEBOOK
  oci_oda_channel:
    # required
    name: name_example
    type: FACEBOOK

    # optional
    app_secret: app_secret_example
    page_access_token: page_access_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = APPLICATION
  oci_oda_channel:
    # required
    name: name_example
    type: APPLICATION

    # optional
    outbound_url: outbound_url_example
    is_authenticated_user_id: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = SERVICECLOUD
  oci_oda_channel:
    # required
    name: name_example
    type: SERVICECLOUD

    # optional
    domain_name: domain_name_example
    host_name_prefix: host_name_prefix_example
    user_name: user_name_example
    password: example-password
    client_type: WSDL
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = SLACK
  oci_oda_channel:
    # required
    name: name_example
    type: SLACK

    # optional
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    auth_success_url: auth_success_url_example
    auth_error_url: auth_error_url_example
    signing_secret: signing_secret_example
    client_secret: client_secret_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = OSVC
  oci_oda_channel:
    # required
    name: name_example
    type: OSVC

    # optional
    host: host_example
    port: port_example
    total_session_count: 56
    channel_service: OSVC
    authentication_provider_name: authentication_provider_name_example
    user_name: user_name_example
    password: example-password
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = APPEVENT
  oci_oda_channel:
    # required
    name: name_example
    type: APPEVENT

    # optional
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = OSS
  oci_oda_channel:
    # required
    name: name_example
    type: OSS

    # optional
    inbound_message_topic: inbound_message_topic_example
    outbound_message_topic: outbound_message_topic_example
    bootstrap_servers: bootstrap_servers_example
    security_protocol: security_protocol_example
    sasl_mechanism: sasl_mechanism_example
    tenancy_name: tenancy_name_example
    stream_pool_id: "ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx"
    event_sink_bot_ids: [ "event_sink_bot_ids_example" ]
    user_name: user_name_example
    auth_token: auth_token_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = CORTANA
  oci_oda_channel:
    # required
    name: name_example
    type: CORTANA

    # optional
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    msa_app_id: "ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx"
    msa_app_password: example-password
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = ANDROID
  oci_oda_channel:
    # required
    name: name_example
    type: ANDROID

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = TWILIO
  oci_oda_channel:
    # required
    name: name_example
    type: TWILIO

    # optional
    account_sid: account_sid_example
    phone_number: phone_number_example
    auth_token: auth_token_example
    is_mms_enabled: true
    original_connectors_url: original_connectors_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = WEBHOOK
  oci_oda_channel:
    # required
    name: name_example
    type: WEBHOOK

    # optional
    payload_version: 1.0
    outbound_url: outbound_url_example
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with type = IOS
  oci_oda_channel:
    # required
    name: name_example
    type: IOS

    # optional
    max_token_expiration_time_in_minutes: 56
    is_client_authentication_enabled: true
    description: description_example
    session_expiry_duration_in_milliseconds: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    bot_id: "ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete channel
  oci_oda_channel:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    channel_id: "ocid1.channel.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete channel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oda_channel:
    # required
    name: name_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient
    from oci.oda.models import CreateChannelDetails
    from oci.oda.models import UpdateChannelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ChannelHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ChannelHelperGen, self).get_possible_entity_types() + [
            "channel",
            "channels",
            "odachannel",
            "odachannels",
            "channelresource",
            "channelsresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "channel_id"

    def get_module_resource_id(self):
        return self.module.params.get("channel_id")

    def get_get_fn(self):
        return self.client.get_channel

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel,
            channel_id=summary_model.id,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_channel,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            channel_id=self.module.params.get("channel_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "oda_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["name"] if self._use_name_as_identifier() else ["name", "type"]
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

    def get_exclude_attributes(self):
        return [
            "page_access_token",
            "password",
            "signing_secret",
            "client_secret",
            "auth_token",
            "app_secret",
            "msa_app_password",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                create_channel_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateChannelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
                update_channel_details=update_details,
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
            call_fn=self.client.delete_channel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                channel_id=self.module.params.get("channel_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ChannelHelperCustom = get_custom_class("ChannelHelperCustom")


class ResourceHelper(ChannelHelperCustom, ChannelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            host=dict(type="str"),
            port=dict(type="str"),
            total_session_count=dict(type="int"),
            channel_service=dict(type="str", choices=["OSVC", "FUSION"]),
            authentication_provider_name=dict(type="str"),
            inbound_message_topic=dict(type="str"),
            outbound_message_topic=dict(type="str"),
            bootstrap_servers=dict(type="str"),
            security_protocol=dict(type="str"),
            sasl_mechanism=dict(type="str"),
            tenancy_name=dict(type="str"),
            stream_pool_id=dict(type="str"),
            event_sink_bot_ids=dict(type="list", elements="str"),
            allowed_domains=dict(type="str"),
            max_token_expiration_time_in_minutes=dict(type="int", no_log=True),
            is_client_authentication_enabled=dict(type="bool"),
            client_id=dict(type="str"),
            auth_success_url=dict(type="str"),
            auth_error_url=dict(type="str"),
            signing_secret=dict(type="str", no_log=True),
            client_secret=dict(type="str", no_log=True),
            domain_name=dict(type="str"),
            host_name_prefix=dict(type="str"),
            user_name=dict(type="str"),
            password=dict(type="str", no_log=True),
            client_type=dict(type="str", choices=["WSDL", "REST"]),
            account_sid=dict(type="str"),
            phone_number=dict(type="str"),
            auth_token=dict(type="str", no_log=True),
            is_mms_enabled=dict(type="bool"),
            original_connectors_url=dict(type="str"),
            payload_version=dict(type="str", choices=["1.0", "1.1"]),
            outbound_url=dict(type="str"),
            is_authenticated_user_id=dict(type="bool"),
            app_secret=dict(type="str", no_log=True),
            page_access_token=dict(type="str", no_log=True),
            description=dict(type="str"),
            type=dict(
                type="str",
                choices=[
                    "MSTEAMS",
                    "WEB",
                    "FACEBOOK",
                    "APPLICATION",
                    "SERVICECLOUD",
                    "SLACK",
                    "OSVC",
                    "APPEVENT",
                    "OSS",
                    "CORTANA",
                    "ANDROID",
                    "TWILIO",
                    "WEBHOOK",
                    "IOS",
                ],
            ),
            session_expiry_duration_in_milliseconds=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            msa_app_id=dict(type="str"),
            msa_app_password=dict(type="str", no_log=True),
            bot_id=dict(type="str"),
            oda_instance_id=dict(type="str", required=True),
            channel_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
