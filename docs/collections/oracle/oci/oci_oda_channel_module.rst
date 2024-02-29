.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na

.. Anchors

.. _ansible_collections.oracle.oci.oci_oda_channel_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_oda_channel -- Manage a Channel resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.42.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_oda_channel`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a Channel resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new Channel.
- This resource has the following action operations in the :ref:`oracle.oci.oci_oda_channel_actions <ansible_collections.oracle.oci.oci_oda_channel_actions_module>` module: rotate_channel_keys, start, stop.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6
- Python SDK for Oracle Cloud Infrastructure https://oracle-cloud-infrastructure-python-sdk.readthedocs.io


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-account_sid"></div>
                    <b>account_sid</b>
                    <a class="ansibleOptionLink" href="#parameter-account_sid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Account SID for the Twilio number.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;TWILIO&#x27;</div>
                                            <div>Required when type is &#x27;TWILIO&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-allowed_domains"></div>
                    <b>allowed_domains</b>
                    <a class="ansibleOptionLink" href="#parameter-allowed_domains" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A comma-delimited whitelist of allowed domains.</div>
                                            <div>The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain.</div>
                                            <div>Typically, you&#x27;d only enter a single asterisk during development. For production, you would add an allowlist of domains.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;WEB&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_user"></div>
                    <b>api_user</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The OCID of the user, on whose behalf, OCI APIs are invoked. If not set, then the value of the OCI_USER_ID environment variable, if any, is used. This option is required if the user is not specified through a configuration file (See <code>config_file_location</code>). To get the user&#x27;s OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_fingerprint"></div>
                    <b>api_user_fingerprint</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_fingerprint" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Fingerprint for the key pair being used. If not set, then the value of the OCI_USER_FINGERPRINT environment variable, if any, is used. This option is required if the key fingerprint is not specified through a configuration file (See <code>config_file_location</code>). To get the key pair&#x27;s fingerprint value please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_file"></div>
                    <b>api_user_key_file</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_file" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Full path and filename of the private key (in PEM format). If not set, then the value of the OCI_USER_KEY_FILE variable, if any, is used. This option is required if the private key is not specified through a configuration file (See <code>config_file_location</code>). If the key is encrypted with a pass-phrase, the <code>api_user_key_pass_phrase</code> option must also be provided.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-api_user_key_pass_phrase"></div>
                    <b>api_user_key_pass_phrase</b>
                    <a class="ansibleOptionLink" href="#parameter-api_user_key_pass_phrase" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Passphrase used by the key referenced in <code>api_user_key_file</code>, if it is encrypted. If not set, then the value of the OCI_USER_KEY_PASS_PHRASE variable, if any, is used. This option is required if the key passphrase is not specified through a configuration file (See <code>config_file_location</code>).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-app_secret"></div>
                    <b>app_secret</b>
                    <a class="ansibleOptionLink" href="#parameter-app_secret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The app secret for your Facebook app.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;FACEBOOK&#x27;</div>
                                            <div>Required when type is &#x27;FACEBOOK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-auth_error_url"></div>
                    <b>auth_error_url</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_error_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The URL to redirect to when authentication is unsuccessful.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SLACK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-auth_purpose"></div>
                    <b>auth_purpose</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_purpose" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>service_principal</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The auth purpose which can be used in conjunction with &#x27;auth_type=instance_principal&#x27;. The default auth_purpose for instance_principal is None.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-auth_success_url"></div>
                    <b>auth_success_url</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_success_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The URL to redirect to when authentication is successful.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SLACK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-auth_token"></div>
                    <b>auth_token</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The authentication token to use when connecting to the Oracle Streaming Service.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;OSS&#x27;, &#x27;TWILIO&#x27;]</div>
                                            <div>Required when type is one of [&#x27;OSS&#x27;, &#x27;TWILIO&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-auth_type"></div>
                    <b>auth_type</b>
                    <a class="ansibleOptionLink" href="#parameter-auth_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>api_key</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>instance_principal</li>
                                                                                                                                                                                                <li>instance_obo_user</li>
                                                                                                                                                                                                <li>resource_principal</li>
                                                                                                                                                                                                <li>security_token</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of authentication to use for making API requests. By default <code>auth_type=&quot;api_key&quot;</code> based authentication is performed and the API key (see <em>api_user_key_file</em>) in your config file will be used. If this &#x27;auth_type&#x27; module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE, if any, is used. Use <code>auth_type=&quot;instance_principal&quot;</code> to use instance principal based authentication when running ansible playbooks within an OCI compute instance.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-authentication_provider_name"></div>
                    <b>authentication_provider_name</b>
                    <a class="ansibleOptionLink" href="#parameter-authentication_provider_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the Authentication Provider to use to authenticate the user.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSVC&#x27;</div>
                                            <div>Required when type is &#x27;OSVC&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bootstrap_servers"></div>
                    <b>bootstrap_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-bootstrap_servers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle Streaming Service bootstrap servers.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-bot_id"></div>
                    <b>bot_id</b>
                    <a class="ansibleOptionLink" href="#parameter-bot_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the Skill or Digital Assistant that the Channel is routed to.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;FACEBOOK&#x27;, &#x27;MSTEAMS&#x27;, &#x27;OSVC&#x27;, &#x27;WEB&#x27;, &#x27;SLACK&#x27;, &#x27;WEBHOOK&#x27;, &#x27;ANDROID&#x27;, &#x27;IOS&#x27;, &#x27;CORTANA&#x27;, &#x27;TWILIO&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-cert_bundle"></div>
                    <b>cert_bundle</b>
                    <a class="ansibleOptionLink" href="#parameter-cert_bundle" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The full path to a CA certificate bundle to be used for SSL verification. This will override the default CA certificate bundle. If not set, then the value of the OCI_ANSIBLE_CERT_BUNDLE variable, if any, is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-channel_id"></div>
                    <b>channel_id</b>
                    <a class="ansibleOptionLink" href="#parameter-channel_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique Channel identifier.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-channel_service"></div>
                    <b>channel_service</b>
                    <a class="ansibleOptionLink" href="#parameter-channel_service" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>OSVC</li>
                                                                                                                                                                                                <li>FUSION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of OSVC service.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSVC&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-client_id"></div>
                    <b>client_id</b>
                    <a class="ansibleOptionLink" href="#parameter-client_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Slack Client Id for the Slack app.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SLACK&#x27;</div>
                                            <div>Required when type is &#x27;SLACK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-client_secret"></div>
                    <b>client_secret</b>
                    <a class="ansibleOptionLink" href="#parameter-client_secret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Client Secret for the Slack App.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SLACK&#x27;</div>
                                            <div>Required when type is &#x27;SLACK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-client_type"></div>
                    <b>client_type</b>
                    <a class="ansibleOptionLink" href="#parameter-client_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>WSDL</li>
                                                                                                                                                                                                <li>REST</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of Service Cloud client.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SERVICECLOUD&#x27;</div>
                                            <div>Required when type is &#x27;SERVICECLOUD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config_file_location"></div>
                    <b>config_file_location</b>
                    <a class="ansibleOptionLink" href="#parameter-config_file_location" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Path to configuration file. If not set then the value of the OCI_CONFIG_FILE environment variable, if any, is used. Otherwise, defaults to ~/.oci/config.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-config_profile_name"></div>
                    <b>config_profile_name</b>
                    <a class="ansibleOptionLink" href="#parameter-config_profile_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The profile to load from the config file referenced by <code>config_file_location</code>. If not set, then the value of the OCI_CONFIG_PROFILE environment variable, if any, is used. Otherwise, defaults to the &quot;DEFAULT&quot; profile in <code>config_file_location</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-defined_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A short description of the Channel.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-domain_name"></div>
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#parameter-domain_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The domain name.</div>
                                            <div>If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.</div>
                                            <div>If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SERVICECLOUD&#x27;</div>
                                            <div>Required when type is &#x27;SERVICECLOUD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-event_sink_bot_ids"></div>
                    <b>event_sink_bot_ids</b>
                    <a class="ansibleOptionLink" href="#parameter-event_sink_bot_ids" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The IDs of the Skills and Digital Assistants that the Channel is routed to.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;APPEVENT&#x27;, &#x27;OSS&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-force_create"></div>
                    <b>force_create</b>
                    <a class="ansibleOptionLink" href="#parameter-force_create" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to attempt non-idempotent creation of a resource. By default, create resource is an idempotent operation, and doesn&#x27;t create the resource if it already exists. Setting this option to true, forcefully creates a copy of the resource, even if it already exists.This option is mutually exclusive with <em>key_by</em>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-freeform_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The host.</div>
                                            <div>For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com.</div>
                                            <div>For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance&#x27;s URL. For example: sitename.exampledomain.com.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSVC&#x27;</div>
                                            <div>Required when type is &#x27;OSVC&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-host_name_prefix"></div>
                    <b>host_name_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-host_name_prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The host prefix.</div>
                                            <div>If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.</div>
                                            <div>If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SERVICECLOUD&#x27;</div>
                                            <div>Required when type is &#x27;SERVICECLOUD&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-inbound_message_topic"></div>
                    <b>inbound_message_topic</b>
                    <a class="ansibleOptionLink" href="#parameter-inbound_message_topic" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The topic inbound messages are received on.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-is_authenticated_user_id"></div>
                    <b>is_authenticated_user_id</b>
                    <a class="ansibleOptionLink" href="#parameter-is_authenticated_user_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>True if the user id in the AIC message should be treated as an authenticated user id.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;APPLICATION&#x27;</div>
                                            <div>Required when type is &#x27;APPLICATION&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-is_client_authentication_enabled"></div>
                    <b>is_client_authentication_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_client_authentication_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether client authentication is enabled or not.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;WEB&#x27;, &#x27;ANDROID&#x27;, &#x27;IOS&#x27;]</div>
                                            <div>Required when type is one of [&#x27;WEB&#x27;, &#x27;ANDROID&#x27;, &#x27;IOS&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-is_mms_enabled"></div>
                    <b>is_mms_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_mms_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether MMS is enabled for this channel or not.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;TWILIO&#x27;</div>
                                            <div>Required when type is &#x27;TWILIO&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-key_by"></div>
                    <b>key_by</b>
                    <a class="ansibleOptionLink" href="#parameter-key_by" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of attributes of this resource which should be used to uniquely identify an instance of the resource. By default, all the attributes of a resource are used to uniquely identify a resource.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-max_token_expiration_time_in_minutes"></div>
                    <b>max_token_expiration_time_in_minutes</b>
                    <a class="ansibleOptionLink" href="#parameter-max_token_expiration_time_in_minutes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum time until the token expires (in minutes).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;WEB&#x27;, &#x27;ANDROID&#x27;, &#x27;IOS&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-msa_app_id"></div>
                    <b>msa_app_id</b>
                    <a class="ansibleOptionLink" href="#parameter-msa_app_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Microsoft App ID that you obtained when you created your bot registration in Azure.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;MSTEAMS&#x27;, &#x27;CORTANA&#x27;]</div>
                                            <div>Required when type is one of [&#x27;MSTEAMS&#x27;, &#x27;CORTANA&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-msa_app_password"></div>
                    <b>msa_app_password</b>
                    <a class="ansibleOptionLink" href="#parameter-msa_app_password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The client secret that you obtained from your bot registration.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;MSTEAMS&#x27;, &#x27;CORTANA&#x27;]</div>
                                            <div>Required when type is one of [&#x27;MSTEAMS&#x27;, &#x27;CORTANA&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Channel&#x27;s name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-oda_instance_id"></div>
                    <b>oda_instance_id</b>
                    <a class="ansibleOptionLink" href="#parameter-oda_instance_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique Digital Assistant instance identifier.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-original_connectors_url"></div>
                    <b>original_connectors_url</b>
                    <a class="ansibleOptionLink" href="#parameter-original_connectors_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The original connectors URL (used for backward compatibility).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;TWILIO&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-outbound_message_topic"></div>
                    <b>outbound_message_topic</b>
                    <a class="ansibleOptionLink" href="#parameter-outbound_message_topic" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The topic outbound messages are sent on.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-outbound_url"></div>
                    <b>outbound_url</b>
                    <a class="ansibleOptionLink" href="#parameter-outbound_url" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The URL to send response and error messages to.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;APPLICATION&#x27;, &#x27;WEBHOOK&#x27;, &#x27;APPEVENT&#x27;]</div>
                                            <div>Required when type is &#x27;WEBHOOK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-page_access_token"></div>
                    <b>page_access_token</b>
                    <a class="ansibleOptionLink" href="#parameter-page_access_token" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The page access token that you generated for your Facebook page.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;FACEBOOK&#x27;</div>
                                            <div>Required when type is &#x27;FACEBOOK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password for the Oracle B2C Service staff member who has the necessary profile permissions.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;OSVC&#x27;, &#x27;SERVICECLOUD&#x27;]</div>
                                            <div>Required when type is one of [&#x27;OSVC&#x27;, &#x27;SERVICECLOUD&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-payload_version"></div>
                    <b>payload_version</b>
                    <a class="ansibleOptionLink" href="#parameter-payload_version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>1.0</li>
                                                                                                                                                                                                <li>1.1</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The version for payloads.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;WEBHOOK&#x27;</div>
                                            <div>Required when type is &#x27;WEBHOOK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-phone_number"></div>
                    <b>phone_number</b>
                    <a class="ansibleOptionLink" href="#parameter-phone_number" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Twilio phone number.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;TWILIO&#x27;</div>
                                            <div>Required when type is &#x27;TWILIO&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The port.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSVC&#x27;</div>
                                            <div>Required when type is &#x27;OSVC&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-realm_specific_endpoint_template_enabled"></div>
                    <b>realm_specific_endpoint_template_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-realm_specific_endpoint_template_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Enable/Disable realm specific endpoint template for service client. By Default, realm specific endpoint template is disabled. If not set, then the value of the OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED variable, if any, is used.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-region"></div>
                    <b>region</b>
                    <a class="ansibleOptionLink" href="#parameter-region" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Oracle Cloud Infrastructure region to use for all OCI API requests. If not set, then the value of the OCI_REGION variable, if any, is used. This option is required if the region is not specified through a configuration file (See <code>config_file_location</code>). Please refer to <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/regions.htm</a> for more information on OCI regions.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-sasl_mechanism"></div>
                    <b>sasl_mechanism</b>
                    <a class="ansibleOptionLink" href="#parameter-sasl_mechanism" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-security_protocol"></div>
                    <b>security_protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-security_protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-session_expiry_duration_in_milliseconds"></div>
                    <b>session_expiry_duration_in_milliseconds</b>
                    <a class="ansibleOptionLink" href="#parameter-session_expiry_duration_in_milliseconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of milliseconds before a session expires.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-signing_secret"></div>
                    <b>signing_secret</b>
                    <a class="ansibleOptionLink" href="#parameter-signing_secret" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Signing Secret for the Slack App.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;SLACK&#x27;</div>
                                            <div>Required when type is &#x27;SLACK&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the Channel.</div>
                                            <div>Use <em>state=present</em> to create or update a Channel.</div>
                                            <div>Use <em>state=absent</em> to delete a Channel.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-stream_pool_id"></div>
                    <b>stream_pool_id</b>
                    <a class="ansibleOptionLink" href="#parameter-stream_pool_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The stream pool OCI to use when connecting to the Oracle Streaming Service.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy"></div>
                    <b>tenancy</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>OCID of your tenancy. If not set, then the value of the OCI_TENANCY variable, if any, is used. This option is required if the tenancy OCID is not specified through a configuration file (See <code>config_file_location</code>). To get the tenancy OCID, please refer <a href='https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm'>https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm</a></div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-tenancy_name"></div>
                    <b>tenancy_name</b>
                    <a class="ansibleOptionLink" href="#parameter-tenancy_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The tenancy to use when connecting to the Oracle Streaming Service.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSS&#x27;</div>
                                            <div>Required when type is &#x27;OSS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-total_session_count"></div>
                    <b>total_session_count</b>
                    <a class="ansibleOptionLink" href="#parameter-total_session_count" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The total session count.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is &#x27;OSVC&#x27;</div>
                                            <div>Required when type is &#x27;OSVC&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>MSTEAMS</li>
                                                                                                                                                                                                <li>WEB</li>
                                                                                                                                                                                                <li>FACEBOOK</li>
                                                                                                                                                                                                <li>APPLICATION</li>
                                                                                                                                                                                                <li>SERVICECLOUD</li>
                                                                                                                                                                                                <li>SLACK</li>
                                                                                                                                                                                                <li>OSVC</li>
                                                                                                                                                                                                <li>APPEVENT</li>
                                                                                                                                                                                                <li>OSS</li>
                                                                                                                                                                                                <li>CORTANA</li>
                                                                                                                                                                                                <li>ANDROID</li>
                                                                                                                                                                                                <li>TWILIO</li>
                                                                                                                                                                                                <li>WEBHOOK</li>
                                                                                                                                                                                                <li>IOS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The Channel type.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with channel_id present.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-user_name"></div>
                    <b>user_name</b>
                    <a class="ansibleOptionLink" href="#parameter-user_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The user name for an Oracle B2C Service staff member who has the necessary profile permissions.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when type is one of [&#x27;OSVC&#x27;, &#x27;SERVICECLOUD&#x27;, &#x27;OSS&#x27;]</div>
                                            <div>Required when type is one of [&#x27;OSVC&#x27;, &#x27;SERVICECLOUD&#x27;, &#x27;OSS&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-wait"></div>
                    <b>wait</b>
                    <a class="ansibleOptionLink" href="#parameter-wait" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to wait for create or delete operation to complete.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-wait_timeout"></div>
                    <b>wait_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Time, in seconds, to wait when <em>wait=yes</em>. Defaults to 1200 for most of the services but some services might have a longer wait timeout.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Attributes


.. Notes

Notes
-----

.. note::
   - For OCI python sdk configuration, please refer to https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/configuration.html

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
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





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-channel"></div>
                    <b>channel</b>
                    <a class="ansibleOptionLink" href="#return-channel" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the Channel resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;account_sid&#x27;: &#x27;account_sid_example&#x27;, &#x27;allowed_domains&#x27;: &#x27;allowed_domains_example&#x27;, &#x27;auth_error_url&#x27;: &#x27;auth_error_url_example&#x27;, &#x27;auth_success_url&#x27;: &#x27;auth_success_url_example&#x27;, &#x27;authentication_provider_name&#x27;: &#x27;authentication_provider_name_example&#x27;, &#x27;bootstrap_servers&#x27;: &#x27;bootstrap_servers_example&#x27;, &#x27;bot_id&#x27;: &#x27;ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;category&#x27;: &#x27;AGENT&#x27;, &#x27;channel_service&#x27;: &#x27;OSVC&#x27;, &#x27;client_id&#x27;: &#x27;ocid1.client.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;client_type&#x27;: &#x27;WSDL&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;domain_name&#x27;: &#x27;domain_name_example&#x27;, &#x27;event_sink_bot_ids&#x27;: [], &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;host&#x27;: &#x27;host_example&#x27;, &#x27;host_name_prefix&#x27;: &#x27;host_name_prefix_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;inbound_message_topic&#x27;: &#x27;inbound_message_topic_example&#x27;, &#x27;is_authenticated_user_id&#x27;: True, &#x27;is_client_authentication_enabled&#x27;: True, &#x27;is_mms_enabled&#x27;: True, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;max_token_expiration_time_in_minutes&#x27;: 56, &#x27;msa_app_id&#x27;: &#x27;ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;original_connectors_url&#x27;: &#x27;original_connectors_url_example&#x27;, &#x27;outbound_message_topic&#x27;: &#x27;outbound_message_topic_example&#x27;, &#x27;outbound_url&#x27;: &#x27;outbound_url_example&#x27;, &#x27;payload_version&#x27;: &#x27;1.0&#x27;, &#x27;phone_number&#x27;: &#x27;phone_number_example&#x27;, &#x27;port&#x27;: &#x27;port_example&#x27;, &#x27;sasl_mechanism&#x27;: &#x27;sasl_mechanism_example&#x27;, &#x27;security_protocol&#x27;: &#x27;security_protocol_example&#x27;, &#x27;session_expiry_duration_in_milliseconds&#x27;: 56, &#x27;stream_pool_id&#x27;: &#x27;ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;tenancy_name&#x27;: &#x27;tenancy_name_example&#x27;, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;total_session_count&#x27;: 56, &#x27;type&#x27;: &#x27;ANDROID&#x27;, &#x27;user_name&#x27;: &#x27;user_name_example&#x27;, &#x27;webhook_url&#x27;: &#x27;webhook_url_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/account_sid"></div>
                    <b>account_sid</b>
                    <a class="ansibleOptionLink" href="#return-channel/account_sid" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Account SID for the Twilio number.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">account_sid_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/allowed_domains"></div>
                    <b>allowed_domains</b>
                    <a class="ansibleOptionLink" href="#return-channel/allowed_domains" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A comma-delimited whitelist of allowed domains.</div>
                                            <div>The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain.</div>
                                            <div>Typically, you&#x27;d only enter a single asterisk during development. For production, you would add an allowlist of domains.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">allowed_domains_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/auth_error_url"></div>
                    <b>auth_error_url</b>
                    <a class="ansibleOptionLink" href="#return-channel/auth_error_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL to redirect to when authentication is unsuccessful.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">auth_error_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/auth_success_url"></div>
                    <b>auth_success_url</b>
                    <a class="ansibleOptionLink" href="#return-channel/auth_success_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL to redirect to when authentication is successful.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">auth_success_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/authentication_provider_name"></div>
                    <b>authentication_provider_name</b>
                    <a class="ansibleOptionLink" href="#return-channel/authentication_provider_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the Authentication Provider to use to authenticate the user.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">authentication_provider_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/bootstrap_servers"></div>
                    <b>bootstrap_servers</b>
                    <a class="ansibleOptionLink" href="#return-channel/bootstrap_servers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Oracle Streaming Service bootstrap servers.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">bootstrap_servers_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/bot_id"></div>
                    <b>bot_id</b>
                    <a class="ansibleOptionLink" href="#return-channel/bot_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ID of the Skill or Digital Assistant that the Channel is routed to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.bot.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/category"></div>
                    <b>category</b>
                    <a class="ansibleOptionLink" href="#return-channel/category" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The category of the Channel.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">AGENT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/channel_service"></div>
                    <b>channel_service</b>
                    <a class="ansibleOptionLink" href="#return-channel/channel_service" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of OSVC service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">OSVC</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/client_id"></div>
                    <b>client_id</b>
                    <a class="ansibleOptionLink" href="#return-channel/client_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Slack Client Id for the Slack app.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.client.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/client_type"></div>
                    <b>client_type</b>
                    <a class="ansibleOptionLink" href="#return-channel/client_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of Service Cloud client.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">WSDL</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-channel/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-channel/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A short description of the Channel.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/domain_name"></div>
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#return-channel/domain_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The domain name.</div>
                                            <div>If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.</div>
                                            <div>If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">domain_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/event_sink_bot_ids"></div>
                    <b>event_sink_bot_ids</b>
                    <a class="ansibleOptionLink" href="#return-channel/event_sink_bot_ids" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The IDs of the Skills and Digital Assistants that the Channel is routed to.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-channel/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#return-channel/host" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The host.</div>
                                            <div>For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com.</div>
                                            <div>For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance&#x27;s URL. For example: sitename.exampledomain.com.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/host_name_prefix"></div>
                    <b>host_name_prefix</b>
                    <a class="ansibleOptionLink" href="#return-channel/host_name_prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The host prefix.</div>
                                            <div>If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.</div>
                                            <div>If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_name_prefix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-channel/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique immutable identifier that was assigned when the Channel was created.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/inbound_message_topic"></div>
                    <b>inbound_message_topic</b>
                    <a class="ansibleOptionLink" href="#return-channel/inbound_message_topic" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The topic inbound messages are received on.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">inbound_message_topic_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/is_authenticated_user_id"></div>
                    <b>is_authenticated_user_id</b>
                    <a class="ansibleOptionLink" href="#return-channel/is_authenticated_user_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>True if the user id in the AIC message should be treated as an authenticated user id.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/is_client_authentication_enabled"></div>
                    <b>is_client_authentication_enabled</b>
                    <a class="ansibleOptionLink" href="#return-channel/is_client_authentication_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether client authentication is enabled or not.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/is_mms_enabled"></div>
                    <b>is_mms_enabled</b>
                    <a class="ansibleOptionLink" href="#return-channel/is_mms_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether MMS is enabled for this channel or not.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-channel/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Channel&#x27;s current state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/max_token_expiration_time_in_minutes"></div>
                    <b>max_token_expiration_time_in_minutes</b>
                    <a class="ansibleOptionLink" href="#return-channel/max_token_expiration_time_in_minutes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum time until the token expires (in minutes).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/msa_app_id"></div>
                    <b>msa_app_id</b>
                    <a class="ansibleOptionLink" href="#return-channel/msa_app_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Microsoft App ID that you obtained when you created your bot registration in Azure.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.msaapp.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-channel/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Channel&#x27;s name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/original_connectors_url"></div>
                    <b>original_connectors_url</b>
                    <a class="ansibleOptionLink" href="#return-channel/original_connectors_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The original connectors URL (used for backward compatibility).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">original_connectors_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/outbound_message_topic"></div>
                    <b>outbound_message_topic</b>
                    <a class="ansibleOptionLink" href="#return-channel/outbound_message_topic" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The topic outbound messages are sent on.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">outbound_message_topic_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/outbound_url"></div>
                    <b>outbound_url</b>
                    <a class="ansibleOptionLink" href="#return-channel/outbound_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL for sending errors and responses to.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">outbound_url_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/payload_version"></div>
                    <b>payload_version</b>
                    <a class="ansibleOptionLink" href="#return-channel/payload_version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The version for payloads.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">1.0</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/phone_number"></div>
                    <b>phone_number</b>
                    <a class="ansibleOptionLink" href="#return-channel/phone_number" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Twilio phone number.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">phone_number_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-channel/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The port.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">port_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/sasl_mechanism"></div>
                    <b>sasl_mechanism</b>
                    <a class="ansibleOptionLink" href="#return-channel/sasl_mechanism" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">sasl_mechanism_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/security_protocol"></div>
                    <b>security_protocol</b>
                    <a class="ansibleOptionLink" href="#return-channel/security_protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">security_protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/session_expiry_duration_in_milliseconds"></div>
                    <b>session_expiry_duration_in_milliseconds</b>
                    <a class="ansibleOptionLink" href="#return-channel/session_expiry_duration_in_milliseconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The number of milliseconds before a session expires.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/stream_pool_id"></div>
                    <b>stream_pool_id</b>
                    <a class="ansibleOptionLink" href="#return-channel/stream_pool_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The stream pool OCI to use when connecting to the Oracle Streaming Service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.streampool.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/tenancy_name"></div>
                    <b>tenancy_name</b>
                    <a class="ansibleOptionLink" href="#return-channel/tenancy_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The tenancy to use when connecting to the Oracle Streaming Service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">tenancy_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-channel/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When the resource was created. A date-time string as described in <a href='https://tools.ietf.org/rfc/rfc3339'>RFC 3339</a>, section 14.29.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-channel/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>When the resource was last updated. A date-time string as described in <a href='https://tools.ietf.org/rfc/rfc3339'>RFC 3339</a>, section 14.29.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/total_session_count"></div>
                    <b>total_session_count</b>
                    <a class="ansibleOptionLink" href="#return-channel/total_session_count" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The total session count.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-channel/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The Channel type.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ANDROID</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/user_name"></div>
                    <b>user_name</b>
                    <a class="ansibleOptionLink" href="#return-channel/user_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The user name to use when connecting to the Oracle Streaming Service.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">user_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-channel/webhook_url"></div>
                    <b>webhook_url</b>
                    <a class="ansibleOptionLink" href="#return-channel/webhook_url" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The URL to use to send messages to this channel. This will be generally be used to configure a webhook in a 3rd party messaging system to send messages to this channel.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">webhook_url_example</div>
                                    </td>
            </tr>
                    
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Oracle (@oracle)



.. Parsing errors

