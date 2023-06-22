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

.. _ansible_collections.oracle.oci.oci_waf_web_app_firewall_policy_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_waf_web_app_firewall_policy -- Manage a WebAppFirewallPolicy resource in Oracle Cloud Infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.25.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_waf_web_app_firewall_policy`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a WebAppFirewallPolicy resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new WebAppFirewallPolicy.
- This resource has the following action operations in the :ref:`oracle.oci.oci_waf_web_app_firewall_policy_actions <ansible_collections.oracle.oci.oci_waf_web_app_firewall_policy_actions_module>` module: change_compartment.


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
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-actions"></div>
                    <b>actions</b>
                    <a class="ansibleOptionLink" href="#parameter-actions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Predefined actions for use in multiple different rules. Not all actions are supported in every module. Some actions terminate further execution of modules and rules in a module and some do not. Actions names must be unique within this array.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/body"></div>
                    <b>body</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/body" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when type is &#x27;RETURN_HTTP_RESPONSE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/body/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/body/text" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Static response body text.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/body/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/body/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STATIC_TEXT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of HttpResponseBody.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/code"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Response code.</div>
                                            <div>The following response codes are valid values for this property:</div>
                                            <div>* 2xx</div>
                                            <div>200 OK 201 Created 202 Accepted 206 Partial Content</div>
                                            <div>* 3xx</div>
                                            <div>300 Multiple Choices 301 Moved Permanently 302 Found 303 See Other 307 Temporary Redirect</div>
                                            <div>* 4xx</div>
                                            <div>400 Bad Request 401 Unauthorized 403 Forbidden 404 Not Found 405 Method Not Allowed 408 Request Timeout 409 Conflict 411 Length Required 412 Precondition Failed 413 Payload Too Large 414 URI Too Long 415 Unsupported Media Type 416 Range Not Satisfiable 422 Unprocessable Entity 429 Too Many Requests 494 Request Header Too Large 495 Cert Error 496 No Cert 497 HTTP to HTTPS</div>
                                            <div>* 5xx</div>
                                            <div>500 Internal Server Error 501 Not Implemented 502 Bad Gateway 503 Service Unavailable 504 Gateway Timeout 507 Insufficient Storage</div>
                                            <div>Example: `200`</div>
                                            <div>Required when type is &#x27;RETURN_HTTP_RESPONSE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Adds headers defined in this array for HTTP response.</div>
                                            <div>Hop-by-hop headers are not allowed to be set:</div>
                                            <div>* Connection * Keep-Alive * Proxy-Authenticate * Proxy-Authorization * TE * Trailer * Transfer-Encoding * Upgrade</div>
                                            <div>Applicable when type is &#x27;RETURN_HTTP_RESPONSE&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/headers/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the header field.</div>
                                            <div>Required when type is &#x27;RETURN_HTTP_RESPONSE&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-actions/headers/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/headers/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of the header field.</div>
                                            <div>Required when type is &#x27;RETURN_HTTP_RESPONSE&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Action name. Can be used to reference the action.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-actions/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-actions/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>RETURN_HTTP_RESPONSE</li>
                                                                                                                                                                                                <li>ALLOW</li>
                                                                                                                                                                                                <li>CHECK</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>* **CHECK** is a non-terminating action that does not stop the execution of rules in current module, just emits a log message documenting result of rule execution.</div>
                                            <div>* **ALLOW** is a non-terminating action which upon matching rule skips all remaining rules in the current module.</div>
                                            <div>* **RETURN_HTTP_RESPONSE** is a terminating action which is executed immediately, returns a defined HTTP response.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#parameter-compartment_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment.</div>
                                            <div>Required for create using <em>state=present</em>.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>Required for delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>WebAppFirewallPolicy display name, can be renamed.</div>
                                            <div>Required for create, update, delete when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control"></div>
                    <b>request_access_control</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/default_action_name"></div>
                    <b>default_action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/default_action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References an default Action to take if no AccessControlRule was matched. Allowed action types:</div>
                                            <div>* **ALLOW** continues execution of other modules and their rules.</div>
                                            <div>* **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules/condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules/condition_language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JMESPATH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_access_control/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-request_access_control/rules/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACCESS_CONTROL</li>
                                                                                                                                                                                                <li>PROTECTION</li>
                                                                                                                                                                                                <li>REQUEST_RATE_LIMITING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection"></div>
                    <b>request_protection</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/body_inspection_size_limit_exceeded_action_name"></div>
                    <b>body_inspection_size_limit_exceeded_action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/body_inspection_size_limit_exceeded_action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy. Executed if HTTP message body size exceeds limit set in field `bodyInspectionSizeLimitInBytes`.</div>
                                            <div>If this field is `null` HTTP message body will inspected up to `bodyInspectionSizeLimitInBytes` and the rest will not be inspected by Protection Capabilities.</div>
                                            <div>Allowed action types: * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/body_inspection_size_limit_in_bytes"></div>
                    <b>body_inspection_size_limit_in_bytes</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/body_inspection_size_limit_in_bytes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum size of inspected HTTP message body in bytes. Actions to take if this limit is exceeded are defined in `bodyInspectionSizeLimitExceededActionName`.</div>
                                            <div>Body inspection maximum size allowed is defined with per-tenancy limit: 8192 bytes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection Capabilities of REQUEST_PROTECTION_CAPABILITY type.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/condition_language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JMESPATH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/is_body_inspection_enabled"></div>
                    <b>is_body_inspection_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/is_body_inspection_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables/disables body inspection for this protection rule. Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will be available at a later date.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities"></div>
                    <b>protection_capabilities</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An ordered list that references OCI-managed protection capabilities. Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order is decided at runtime for improved performance. The array cannot contain entries with the same pair of capability key and version more than once.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Override action to take if capability was triggered, defined in Protection Rule for this capability. Only actions of type CHECK are allowed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/collaborative_action_threshold"></div>
                    <b>collaborative_action_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/collaborative_action_threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum sum of weights of associated collaborative protection capabilities that have triggered which must be reached in order for _this_ capability to trigger. This field is ignored for non-collaborative capabilities.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/collaborative_weights"></div>
                    <b>collaborative_weights</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/collaborative_weights" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Explicit weight values to use for associated collaborative protection capabilities.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/collaborative_weights/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/collaborative_weights/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique key of collaborative capability for which weight will be overridden.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/collaborative_weights/weight"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/collaborative_weights/weight" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of weight to set.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/exclusions"></div>
                    <b>exclusions</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/exclusions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/exclusions/args"></div>
                    <b>args</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/exclusions/args" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting. Example: If we have query parameter &#x27;argumentName=argumentValue&#x27; and args=[&#x27;argumentName&#x27;], both &#x27;argumentName&#x27; and &#x27;argumentValue&#x27; will not be inspected.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/exclusions/request_cookies"></div>
                    <b>request_cookies</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/exclusions/request_cookies" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of HTTP request cookie values (by cookie name) to exclude from inspecting. Example: If we have cookie &#x27;cookieName=cookieValue&#x27; and requestCookies=[&#x27;cookieName&#x27;], both &#x27;cookieName&#x27; and &#x27;cookieValue&#x27; will not be inspected.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique key of referenced protection capability.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capabilities/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capabilities/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Version of referenced protection capability.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings"></div>
                    <b>protection_capability_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/allowed_http_methods"></div>
                    <b>allowed_http_methods</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/allowed_http_methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of allowed HTTP methods. Each value as a RFC7230 formated token string. Used in protection capability 911100: Restrict HTTP Request Methods.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/max_http_request_header_length"></div>
                    <b>max_http_request_header_length</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/max_http_request_header_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/max_http_request_headers"></div>
                    <b>max_http_request_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/max_http_request_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/max_number_of_arguments"></div>
                    <b>max_number_of_arguments</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/max_number_of_arguments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/max_single_argument_length"></div>
                    <b>max_single_argument_length</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/max_single_argument_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/protection_capability_settings/max_total_argument_length"></div>
                    <b>max_total_argument_length</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/protection_capability_settings/max_total_argument_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_protection/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-request_protection/rules/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACCESS_CONTROL</li>
                                                                                                                                                                                                <li>PROTECTION</li>
                                                                                                                                                                                                <li>REQUEST_RATE_LIMITING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting"></div>
                    <b>request_rate_limiting</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/condition_language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JMESPATH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/configurations"></div>
                    <b>configurations</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/configurations" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rate Limiting Configurations. Each configuration counts requests towards its own `requestsLimit`.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/configurations/action_duration_in_seconds"></div>
                    <b>action_duration_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/configurations/action_duration_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Duration of block action application in seconds when `requestsLimit` is reached. Optional and can be 0 (no block duration).</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/configurations/period_in_seconds"></div>
                    <b>period_in_seconds</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/configurations/period_in_seconds" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Evaluation period in seconds.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/configurations/requests_limit"></div>
                    <b>requests_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/configurations/requests_limit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Requests allowed per evaluation period.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-request_rate_limiting/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-request_rate_limiting/rules/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACCESS_CONTROL</li>
                                                                                                                                                                                                <li>PROTECTION</li>
                                                                                                                                                                                                <li>REQUEST_RATE_LIMITING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control"></div>
                    <b>response_access_control</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules/condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules/condition_language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JMESPATH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_access_control/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-response_access_control/rules/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACCESS_CONTROL</li>
                                                                                                                                                                                                <li>PROTECTION</li>
                                                                                                                                                                                                <li>REQUEST_RATE_LIMITING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection"></div>
                    <b>response_protection</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection capabilities of RESPONSE_PROTECTION_CAPABILITY type.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/condition" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/condition_language" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>JMESPATH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/is_body_inspection_enabled"></div>
                    <b>is_body_inspection_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/is_body_inspection_enabled" title="Permalink to this option"></a>
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
                                            <div>Enables/disables body inspection for this protection rule. Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will be available at a later date.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities"></div>
                    <b>protection_capabilities</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                         / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An ordered list that references OCI-managed protection capabilities. Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order is decided at runtime for improved performance. The array cannot contain entries with the same pair of capability key and version more than once.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/action_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Override action to take if capability was triggered, defined in Protection Rule for this capability. Only actions of type CHECK are allowed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/collaborative_action_threshold"></div>
                    <b>collaborative_action_threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/collaborative_action_threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The minimum sum of weights of associated collaborative protection capabilities that have triggered which must be reached in order for _this_ capability to trigger. This field is ignored for non-collaborative capabilities.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/collaborative_weights"></div>
                    <b>collaborative_weights</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/collaborative_weights" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Explicit weight values to use for associated collaborative protection capabilities.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/collaborative_weights/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/collaborative_weights/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique key of collaborative capability for which weight will be overridden.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/collaborative_weights/weight"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/collaborative_weights/weight" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The value of weight to set.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/exclusions"></div>
                    <b>exclusions</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/exclusions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/exclusions/args"></div>
                    <b>args</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/exclusions/args" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting. Example: If we have query parameter &#x27;argumentName=argumentValue&#x27; and args=[&#x27;argumentName&#x27;], both &#x27;argumentName&#x27; and &#x27;argumentValue&#x27; will not be inspected.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/exclusions/request_cookies"></div>
                    <b>request_cookies</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/exclusions/request_cookies" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of HTTP request cookie values (by cookie name) to exclude from inspecting. Example: If we have cookie &#x27;cookieName=cookieValue&#x27; and requestCookies=[&#x27;cookieName&#x27;], both &#x27;cookieName&#x27; and &#x27;cookieValue&#x27; will not be inspected.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/key" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique key of referenced protection capability.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capabilities/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capabilities/version" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Version of referenced protection capability.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings"></div>
                    <b>protection_capability_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/allowed_http_methods"></div>
                    <b>allowed_http_methods</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/allowed_http_methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of allowed HTTP methods. Each value as a RFC7230 formated token string. Used in protection capability 911100: Restrict HTTP Request Methods.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/max_http_request_header_length"></div>
                    <b>max_http_request_header_length</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/max_http_request_header_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/max_http_request_headers"></div>
                    <b>max_http_request_headers</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/max_http_request_headers" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/max_number_of_arguments"></div>
                    <b>max_number_of_arguments</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/max_number_of_arguments" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/max_single_argument_length"></div>
                    <b>max_single_argument_length</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/max_single_argument_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/protection_capability_settings/max_total_argument_length"></div>
                    <b>max_total_argument_length</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/protection_capability_settings/max_total_argument_length" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-response_protection/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-response_protection/rules/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ACCESS_CONTROL</li>
                                                                                                                                                                                                <li>PROTECTION</li>
                                                                                                                                                                                                <li>REQUEST_RATE_LIMITING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                                        </td>
            </tr>
                    
                    
                                <tr>
                                                                <td colspan="5">
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
                                            <div>The state of the WebAppFirewallPolicy.</div>
                                            <div>Use <em>state=present</em> to create or update a WebAppFirewallPolicy.</div>
                                            <div>Use <em>state=absent</em> to delete a WebAppFirewallPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#parameter-system_tags" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                                                <td colspan="5">
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
                                <tr>
                                                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-web_app_firewall_policy_id"></div>
                    <b>web_app_firewall_policy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-web_app_firewall_policy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the WebAppFirewallPolicy.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                            <div>Required for delete using <em>state=absent</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
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

    
    - name: Create web_app_firewall_policy
      oci_waf_web_app_firewall_policy:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        actions:
        - # required
          code: 56
          type: RETURN_HTTP_RESPONSE
          name: name_example

          # optional
          headers:
          - # required
            name: name_example
            value: value_example
          body:
            # required
            type: STATIC_TEXT
            text: text_example
        request_access_control:
          # required
          default_action_name: default_action_name_example

          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_rate_limiting:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            configurations:
            - # required
              period_in_seconds: 56
              requests_limit: 56

              # optional
              action_duration_in_seconds: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
          body_inspection_size_limit_in_bytes: 56
          body_inspection_size_limit_exceeded_action_name: body_inspection_size_limit_exceeded_action_name_example
        response_access_control:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        response_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        system_tags: null

    - name: Update web_app_firewall_policy
      oci_waf_web_app_firewall_policy:
        # required
        web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        display_name: display_name_example
        actions:
        - # required
          code: 56
          type: RETURN_HTTP_RESPONSE
          name: name_example

          # optional
          headers:
          - # required
            name: name_example
            value: value_example
          body:
            # required
            type: STATIC_TEXT
            text: text_example
        request_access_control:
          # required
          default_action_name: default_action_name_example

          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_rate_limiting:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            configurations:
            - # required
              period_in_seconds: 56
              requests_limit: 56

              # optional
              action_duration_in_seconds: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
          body_inspection_size_limit_in_bytes: 56
          body_inspection_size_limit_exceeded_action_name: body_inspection_size_limit_exceeded_action_name_example
        response_access_control:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        response_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        system_tags: null

    - name: Update web_app_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_waf_web_app_firewall_policy:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example

        # optional
        actions:
        - # required
          code: 56
          type: RETURN_HTTP_RESPONSE
          name: name_example

          # optional
          headers:
          - # required
            name: name_example
            value: value_example
          body:
            # required
            type: STATIC_TEXT
            text: text_example
        request_access_control:
          # required
          default_action_name: default_action_name_example

          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_rate_limiting:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            configurations:
            - # required
              period_in_seconds: 56
              requests_limit: 56

              # optional
              action_duration_in_seconds: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
        request_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
          body_inspection_size_limit_in_bytes: 56
          body_inspection_size_limit_exceeded_action_name: body_inspection_size_limit_exceeded_action_name_example
        response_access_control:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example

            # optional
            condition_language: JMESPATH
            condition: condition_example
        response_protection:
          # optional
          rules:
          - # required
            type: ACCESS_CONTROL
            name: name_example
            action_name: action_name_example
            protection_capabilities:
            - # required
              key: key_example
              version: 56

              # optional
              exclusions:
                # optional
                request_cookies: [ "request_cookies_example" ]
                args: [ "args_example" ]
              action_name: action_name_example
              collaborative_action_threshold: 56
              collaborative_weights:
              - # required
                key: key_example
                weight: 56

            # optional
            condition_language: JMESPATH
            condition: condition_example
            protection_capability_settings:
              # optional
              max_number_of_arguments: 56
              max_single_argument_length: 56
              max_total_argument_length: 56
              max_http_request_headers: 56
              max_http_request_header_length: 56
              allowed_http_methods: [ "allowed_http_methods_example" ]
            is_body_inspection_enabled: true
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        system_tags: null

    - name: Delete web_app_firewall_policy
      oci_waf_web_app_firewall_policy:
        # required
        web_app_firewall_policy_id: "ocid1.webappfirewallpolicy.oc1..xxxxxxEXAMPLExxxxxx"
        state: absent

    - name: Delete web_app_firewall_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
      oci_waf_web_app_firewall_policy:
        # required
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        state: absent





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy"></div>
                    <b>web_app_firewall_policy</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the WebAppFirewallPolicy resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;actions&#x27;: [{&#x27;body&#x27;: {&#x27;text&#x27;: &#x27;text_example&#x27;, &#x27;type&#x27;: &#x27;STATIC_TEXT&#x27;}, &#x27;code&#x27;: 56, &#x27;headers&#x27;: [{&#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;type&#x27;: &#x27;CHECK&#x27;}], &#x27;compartment_id&#x27;: &#x27;ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;defined_tags&#x27;: {&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;freeform_tags&#x27;: {&#x27;Department&#x27;: &#x27;Finance&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;lifecycle_details&#x27;: &#x27;lifecycle_details_example&#x27;, &#x27;lifecycle_state&#x27;: &#x27;CREATING&#x27;, &#x27;request_access_control&#x27;: {&#x27;default_action_name&#x27;: &#x27;default_action_name_example&#x27;, &#x27;rules&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;condition_language&#x27;: &#x27;JMESPATH&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;type&#x27;: &#x27;ACCESS_CONTROL&#x27;}]}, &#x27;request_protection&#x27;: {&#x27;body_inspection_size_limit_exceeded_action_name&#x27;: &#x27;body_inspection_size_limit_exceeded_action_name_example&#x27;, &#x27;body_inspection_size_limit_in_bytes&#x27;: 56, &#x27;rules&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;condition_language&#x27;: &#x27;JMESPATH&#x27;, &#x27;is_body_inspection_enabled&#x27;: True, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;protection_capabilities&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;collaborative_action_threshold&#x27;: 56, &#x27;collaborative_weights&#x27;: [{&#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;weight&#x27;: 56}], &#x27;exclusions&#x27;: {&#x27;args&#x27;: [], &#x27;request_cookies&#x27;: []}, &#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;version&#x27;: 56}], &#x27;protection_capability_settings&#x27;: {&#x27;allowed_http_methods&#x27;: [], &#x27;max_http_request_header_length&#x27;: 56, &#x27;max_http_request_headers&#x27;: 56, &#x27;max_number_of_arguments&#x27;: 56, &#x27;max_single_argument_length&#x27;: 56, &#x27;max_total_argument_length&#x27;: 56}, &#x27;type&#x27;: &#x27;ACCESS_CONTROL&#x27;}]}, &#x27;request_rate_limiting&#x27;: {&#x27;rules&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;condition_language&#x27;: &#x27;JMESPATH&#x27;, &#x27;configurations&#x27;: [{&#x27;action_duration_in_seconds&#x27;: 56, &#x27;period_in_seconds&#x27;: 56, &#x27;requests_limit&#x27;: 56}], &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;type&#x27;: &#x27;ACCESS_CONTROL&#x27;}]}, &#x27;response_access_control&#x27;: {&#x27;rules&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;condition_language&#x27;: &#x27;JMESPATH&#x27;, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;type&#x27;: &#x27;ACCESS_CONTROL&#x27;}]}, &#x27;response_protection&#x27;: {&#x27;rules&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;condition&#x27;: &#x27;condition_example&#x27;, &#x27;condition_language&#x27;: &#x27;JMESPATH&#x27;, &#x27;is_body_inspection_enabled&#x27;: True, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;protection_capabilities&#x27;: [{&#x27;action_name&#x27;: &#x27;action_name_example&#x27;, &#x27;collaborative_action_threshold&#x27;: 56, &#x27;collaborative_weights&#x27;: [{&#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;weight&#x27;: 56}], &#x27;exclusions&#x27;: {&#x27;args&#x27;: [], &#x27;request_cookies&#x27;: []}, &#x27;key&#x27;: &#x27;key_example&#x27;, &#x27;version&#x27;: 56}], &#x27;protection_capability_settings&#x27;: {&#x27;allowed_http_methods&#x27;: [], &#x27;max_http_request_header_length&#x27;: 56, &#x27;max_http_request_headers&#x27;: 56, &#x27;max_number_of_arguments&#x27;: 56, &#x27;max_single_argument_length&#x27;: 56, &#x27;max_total_argument_length&#x27;: 56}, &#x27;type&#x27;: &#x27;ACCESS_CONTROL&#x27;}]}, &#x27;system_tags&#x27;: {}, &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;, &#x27;time_updated&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions"></div>
                    <b>actions</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Predefined actions for use in multiple different rules. Not all actions are supported in every module. Some actions terminate further execution of modules and rules in a module and some do not. Actions names must be unique within this array.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/body"></div>
                    <b>body</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/body" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/body/text"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/body/text" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Static response body text.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">text_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/body/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/body/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of HttpResponseBody.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STATIC_TEXT</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/code"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Response code.</div>
                                            <div>The following response codes are valid values for this property:</div>
                                            <div>* 2xx</div>
                                            <div>200 OK 201 Created 202 Accepted 206 Partial Content</div>
                                            <div>* 3xx</div>
                                            <div>300 Multiple Choices 301 Moved Permanently 302 Found 303 See Other 307 Temporary Redirect</div>
                                            <div>* 4xx</div>
                                            <div>400 Bad Request 401 Unauthorized 403 Forbidden 404 Not Found 405 Method Not Allowed 408 Request Timeout 409 Conflict 411 Length Required 412 Precondition Failed 413 Payload Too Large 414 URI Too Long 415 Unsupported Media Type 416 Range Not Satisfiable 422 Unprocessable Entity 429 Too Many Requests 494 Request Header Too Large 495 Cert Error 496 No Cert 497 HTTP to HTTPS</div>
                                            <div>* 5xx</div>
                                            <div>500 Internal Server Error 501 Not Implemented 502 Bad Gateway 503 Service Unavailable 504 Gateway Timeout 507 Insufficient Storage</div>
                                            <div>Example: `200`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/headers"></div>
                    <b>headers</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Adds headers defined in this array for HTTP response.</div>
                                            <div>Hop-by-hop headers are not allowed to be set:</div>
                                            <div>* Connection * Keep-Alive * Proxy-Authenticate * Proxy-Authorization * TE * Trailer * Transfer-Encoding * Upgrade</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/headers/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/headers/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the header field.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/headers/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/headers/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The value of the header field.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Action name. Can be used to reference the action.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/actions/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/actions/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>* **CHECK** is a non-terminating action that does not stop the execution of rules in current module, just emits a log message documenting result of rule execution.</div>
                                            <div>* **ALLOW** is a non-terminating action which upon matching rule skips all remaining rules in the current module.</div>
                                            <div>* **RETURN_HTTP_RESPONSE** is a terminating action which is executed immediately, returns a defined HTTP response.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CHECK</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/compartment_id"></div>
                    <b>compartment_id</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/compartment_id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the compartment.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/defined_tags"></div>
                    <b>defined_tags</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/defined_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{&quot;foo-namespace&quot;: {&quot;bar-key&quot;: &quot;value&quot;}}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Operations&#x27;: {&#x27;CostCenter&#x27;: &#x27;US&#x27;}}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>WebAppFirewallPolicy display name, can be renamed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/freeform_tags"></div>
                    <b>freeform_tags</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/freeform_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{&quot;bar-key&quot;: &quot;value&quot;}`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;Department&#x27;: &#x27;Finance&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/lifecycle_details"></div>
                    <b>lifecycle_details</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/lifecycle_details" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in FAILED state.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">lifecycle_details_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/lifecycle_state"></div>
                    <b>lifecycle_state</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/lifecycle_state" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The current state of the WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CREATING</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control"></div>
                    <b>request_access_control</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/default_action_name"></div>
                    <b>default_action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/default_action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References an default Action to take if no AccessControlRule was matched. Allowed action types:</div>
                                            <div>* **ALLOW** continues execution of other modules and their rules.</div>
                                            <div>* **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">default_action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules/condition_language" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JMESPATH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_access_control/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_access_control/rules/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACCESS_CONTROL</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection"></div>
                    <b>request_protection</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/body_inspection_size_limit_exceeded_action_name"></div>
                    <b>body_inspection_size_limit_exceeded_action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/body_inspection_size_limit_exceeded_action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy. Executed if HTTP message body size exceeds limit set in field `bodyInspectionSizeLimitInBytes`.</div>
                                            <div>If this field is `null` HTTP message body will inspected up to `bodyInspectionSizeLimitInBytes` and the rest will not be inspected by Protection Capabilities.</div>
                                            <div>Allowed action types: * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">body_inspection_size_limit_exceeded_action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/body_inspection_size_limit_in_bytes"></div>
                    <b>body_inspection_size_limit_in_bytes</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/body_inspection_size_limit_in_bytes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum size of inspected HTTP message body in bytes. Actions to take if this limit is exceeded are defined in `bodyInspectionSizeLimitExceededActionName`.</div>
                                            <div>Body inspection maximum size allowed is defined with per-tenancy limit: 8192 bytes.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection Capabilities of REQUEST_PROTECTION_CAPABILITY type.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/condition_language" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JMESPATH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/is_body_inspection_enabled"></div>
                    <b>is_body_inspection_enabled</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/is_body_inspection_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables/disables body inspection for this protection rule. Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will be available at a later date.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities"></div>
                    <b>protection_capabilities</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An ordered list that references OCI-managed protection capabilities. Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order is decided at runtime for improved performance. The array cannot contain entries with the same pair of capability key and version more than once.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Override action to take if capability was triggered, defined in Protection Rule for this capability. Only actions of type CHECK are allowed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_action_threshold"></div>
                    <b>collaborative_action_threshold</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_action_threshold" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum sum of weights of associated collaborative protection capabilities that have triggered which must be reached in order for _this_ capability to trigger. This field is ignored for non-collaborative capabilities.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights"></div>
                    <b>collaborative_weights</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Explicit weight values to use for associated collaborative protection capabilities.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique key of collaborative capability for which weight will be overridden.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights/weight"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/collaborative_weights/weight" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The value of weight to set.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions"></div>
                    <b>exclusions</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions/args"></div>
                    <b>args</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions/args" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting. Example: If we have query parameter &#x27;argumentName=argumentValue&#x27; and args=[&#x27;argumentName&#x27;], both &#x27;argumentName&#x27; and &#x27;argumentValue&#x27; will not be inspected.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions/request_cookies"></div>
                    <b>request_cookies</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/exclusions/request_cookies" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of HTTP request cookie values (by cookie name) to exclude from inspecting. Example: If we have cookie &#x27;cookieName=cookieValue&#x27; and requestCookies=[&#x27;cookieName&#x27;], both &#x27;cookieName&#x27; and &#x27;cookieValue&#x27; will not be inspected.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique key of referenced protection capability.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capabilities/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capabilities/version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Version of referenced protection capability.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings"></div>
                    <b>protection_capability_settings</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/allowed_http_methods"></div>
                    <b>allowed_http_methods</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/allowed_http_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of allowed HTTP methods. Each value as a RFC7230 formated token string. Used in protection capability 911100: Restrict HTTP Request Methods.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_http_request_header_length"></div>
                    <b>max_http_request_header_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_http_request_header_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_http_request_headers"></div>
                    <b>max_http_request_headers</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_http_request_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_number_of_arguments"></div>
                    <b>max_number_of_arguments</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_number_of_arguments" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_single_argument_length"></div>
                    <b>max_single_argument_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_single_argument_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_total_argument_length"></div>
                    <b>max_total_argument_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/protection_capability_settings/max_total_argument_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_protection/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_protection/rules/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACCESS_CONTROL</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting"></div>
                    <b>request_rate_limiting</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ordered list of RequestRateLimitingRules. Rules are executed in order of appearance in this array.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/condition_language" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JMESPATH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/configurations"></div>
                    <b>configurations</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/configurations" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rate Limiting Configurations. Each configuration counts requests towards its own `requestsLimit`.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/configurations/action_duration_in_seconds"></div>
                    <b>action_duration_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/configurations/action_duration_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Duration of block action application in seconds when `requestsLimit` is reached. Optional and can be 0 (no block duration).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/configurations/period_in_seconds"></div>
                    <b>period_in_seconds</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/configurations/period_in_seconds" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Evaluation period in seconds.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/configurations/requests_limit"></div>
                    <b>requests_limit</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/configurations/requests_limit" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Requests allowed per evaluation period.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/request_rate_limiting/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/request_rate_limiting/rules/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACCESS_CONTROL</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control"></div>
                    <b>response_access_control</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules/condition_language" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JMESPATH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_access_control/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_access_control/rules/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACCESS_CONTROL</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection"></div>
                    <b>response_protection</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Ordered list of ProtectionRules. Rules are executed in order of appearance in this array. ProtectionRules in this array can only use protection capabilities of RESPONSE_PROTECTION_CAPABILITY type.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>References action by name from actions defined in WebAppFirewallPolicy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/condition"></div>
                    <b>condition</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/condition" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An expression that determines whether or not the rule action should be executed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">condition_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/condition_language"></div>
                    <b>condition_language</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/condition_language" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The language used to parse condition from field `condition`. Available languages:</div>
                                            <div>* **JMESPATH** an extended JMESPath language syntax.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">JMESPATH</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/is_body_inspection_enabled"></div>
                    <b>is_body_inspection_enabled</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/is_body_inspection_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Enables/disables body inspection for this protection rule. Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will be available at a later date.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Rule name. Must be unique within the module.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities"></div>
                    <b>protection_capabilities</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An ordered list that references OCI-managed protection capabilities. Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order is decided at runtime for improved performance. The array cannot contain entries with the same pair of capability key and version more than once.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/action_name"></div>
                    <b>action_name</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/action_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Override action to take if capability was triggered, defined in Protection Rule for this capability. Only actions of type CHECK are allowed.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_action_threshold"></div>
                    <b>collaborative_action_threshold</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_action_threshold" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The minimum sum of weights of associated collaborative protection capabilities that have triggered which must be reached in order for _this_ capability to trigger. This field is ignored for non-collaborative capabilities.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights"></div>
                    <b>collaborative_weights</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Explicit weight values to use for associated collaborative protection capabilities.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique key of collaborative capability for which weight will be overridden.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights/weight"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/collaborative_weights/weight" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The value of weight to set.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions"></div>
                    <b>exclusions</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions/args"></div>
                    <b>args</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions/args" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of URL query parameter values from form-urlencoded XML, JSON, AMP, or POST payloads to exclude from inspecting. Example: If we have query parameter &#x27;argumentName=argumentValue&#x27; and args=[&#x27;argumentName&#x27;], both &#x27;argumentName&#x27; and &#x27;argumentValue&#x27; will not be inspected.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions/request_cookies"></div>
                    <b>request_cookies</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/exclusions/request_cookies" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of HTTP request cookie values (by cookie name) to exclude from inspecting. Example: If we have cookie &#x27;cookieName=cookieValue&#x27; and requestCookies=[&#x27;cookieName&#x27;], both &#x27;cookieName&#x27; and &#x27;cookieValue&#x27; will not be inspected.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/key"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/key" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Unique key of referenced protection capability.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">key_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capabilities/version"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capabilities/version" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Version of referenced protection capability.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings"></div>
                    <b>protection_capability_settings</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/allowed_http_methods"></div>
                    <b>allowed_http_methods</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/allowed_http_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>List of allowed HTTP methods. Each value as a RFC7230 formated token string. Used in protection capability 911100: Restrict HTTP Request Methods.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_http_request_header_length"></div>
                    <b>max_http_request_header_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_http_request_header_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed length of headers in an HTTP request. Used in protection capability: 9200024: Limit length of request header size.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_http_request_headers"></div>
                    <b>max_http_request_headers</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_http_request_headers" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of headers allowed in an HTTP request. Used in protection capability 9200014: Limit Number of Request Headers.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_number_of_arguments"></div>
                    <b>max_number_of_arguments</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_number_of_arguments" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum number of arguments allowed. Used in protection capability 920380: Number of Arguments Limits.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_single_argument_length"></div>
                    <b>max_single_argument_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_single_argument_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed length of a single argument. Used in protection capability 920370: Limit argument value length.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_total_argument_length"></div>
                    <b>max_total_argument_length</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/protection_capability_settings/max_total_argument_length" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Maximum allowed total length of all arguments. Used in protection capability 920390: Limit arguments total length.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/response_protection/rules/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/response_protection/rules/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Type of WebAppFirewallPolicyRule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ACCESS_CONTROL</div>
                                    </td>
            </tr>
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/system_tags"></div>
                    <b>system_tags</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/system_tags" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{&quot;orcl-cloud&quot;: {&quot;free-tier-retained&quot;: &quot;true&quot;}}`</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-web_app_firewall_policy/time_updated"></div>
                    <b>time_updated</b>
                    <a class="ansibleOptionLink" href="#return-web_app_firewall_policy/time_updated" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2013-10-20T19:20:30+01:00</div>
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

