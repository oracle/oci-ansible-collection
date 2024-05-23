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

.. _ansible_collections.oracle.oci.oci_loadbalancer_rule_set_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_loadbalancer_rule_set -- Manage a RuleSet resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.1.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_loadbalancer_rule_set`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to create, update and delete a RuleSet resource in Oracle Cloud Infrastructure
- For *state=present*, creates a new rule set associated with the specified load balancer. For more information, see `Managing Rule Sets <https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm>`_.


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
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#parameter-items" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of rules that compose the rule set.</div>
                                            <div>Required for create using <em>state=present</em>, update using <em>state=present</em> with name present.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-items/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>ADD_HTTP_REQUEST_HEADER</li>
                                                                                                                                                                                                <li>REDIRECT</li>
                                                                                                                                                                                                <li>REMOVE_HTTP_REQUEST_HEADER</li>
                                                                                                                                                                                                <li>EXTEND_HTTP_REQUEST_HEADER_VALUE</li>
                                                                                                                                                                                                <li>REMOVE_HTTP_RESPONSE_HEADER</li>
                                                                                                                                                                                                <li>CONTROL_ACCESS_USING_HTTP_METHODS</li>
                                                                                                                                                                                                <li>ALLOW</li>
                                                                                                                                                                                                <li>HTTP_HEADER</li>
                                                                                                                                                                                                <li>ADD_HTTP_RESPONSE_HEADER</li>
                                                                                                                                                                                                <li>EXTEND_HTTP_RESPONSE_HEADER_VALUE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#parameter-items/allowed_methods" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The list of HTTP methods allowed for this listener.</div>
                                            <div>By default, you can specify only the standard HTTP methods defined in the <a href='http://www.iana.org/assignments/http-methods/http-methods.xhtml'>HTTP Method Registry</a>. You can also see a list of supported standard HTTP methods in the Load Balancing service documentation at <a href='https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm'>Managing Rule Sets</a>.</div>
                                            <div>Your backend application must be able to handle the methods specified in this list.</div>
                                            <div>The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact <a href='http://support.oracle.com/'>My Oracle Support</a> to remove the restriction for your tenancy.</div>
                                            <div>Example: [&quot;GET&quot;, &quot;PUT&quot;, &quot;POST&quot;, &quot;PROPFIND&quot;]</div>
                                            <div>Required when action is &#x27;CONTROL_ACCESS_USING_HTTP_METHODS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/are_invalid_characters_allowed"></div>
                    <b>are_invalid_characters_allowed</b>
                    <a class="ansibleOptionLink" href="#parameter-items/are_invalid_characters_allowed" title="Permalink to this option"></a>
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
                                            <div>Indicates whether or not invalid characters in client header fields will be allowed. Valid names are composed of English letters, digits, hyphens and underscores. If &quot;true&quot;, invalid characters are allowed in the HTTP header. If &quot;false&quot;, invalid characters are not allowed in the HTTP header</div>
                                            <div>Applicable when action is &#x27;HTTP_HEADER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/conditions"></div>
                    <b>conditions</b>
                    <a class="ansibleOptionLink" href="#parameter-items/conditions" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when action is one of [&#x27;REDIRECT&#x27;, &#x27;ALLOW&#x27;]</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/conditions/attribute_name"></div>
                    <b>attribute_name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/conditions/attribute_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>SOURCE_VCN_ID</li>
                                                                                                                                                                                                <li>SOURCE_IP_ADDRESS</li>
                                                                                                                                                                                                <li>PATH</li>
                                                                                                                                                                                                <li>SOURCE_VCN_IP_ADDRESS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div></div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/conditions/attribute_value"></div>
                    <b>attribute_value</b>
                    <a class="ansibleOptionLink" href="#parameter-items/conditions/attribute_value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the originating VCN that an incoming packet must match.</div>
                                            <div>You can use this condition in conjunction with `SourceVcnIpAddressCondition`.</div>
                                            <div>**NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition matches all incoming traffic in the specified VCN.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/conditions/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-items/conditions/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>EXACT_MATCH</li>
                                                                                                                                                                                                <li>FORCE_LONGEST_PREFIX_MATCH</li>
                                                                                                                                                                                                <li>PREFIX_MATCH</li>
                                                                                                                                                                                                <li>SUFFIX_MATCH</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A string that specifies how to compare the PathMatchCondition object&#x27;s `attributeValue` string to the incoming URI.</div>
                                            <div>*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string.</div>
                                            <div>*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best, longest match of the beginning portion of the incoming URI path.</div>
                                            <div>*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                            <div>*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                            <div>Required when attribute_name is &#x27;PATH&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-items/description" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A brief description of the access control rule. Avoid entering confidential information.</div>
                                            <div>example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`</div>
                                            <div>Applicable when action is &#x27;ALLOW&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/header"></div>
                    <b>header</b>
                    <a class="ansibleOptionLink" href="#parameter-items/header" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A header name that conforms to RFC 7230.</div>
                                            <div>Example: `example_header_name`</div>
                                            <div>Required when action is one of [&#x27;REMOVE_HTTP_REQUEST_HEADER&#x27;, &#x27;EXTEND_HTTP_REQUEST_HEADER_VALUE&#x27;, &#x27;ADD_HTTP_RESPONSE_HEADER&#x27;, &#x27;ADD_HTTP_REQUEST_HEADER&#x27;, &#x27;REMOVE_HTTP_RESPONSE_HEADER&#x27;, &#x27;EXTEND_HTTP_RESPONSE_HEADER_VALUE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/http_large_header_size_in_kb"></div>
                    <b>http_large_header_size_in_kb</b>
                    <a class="ansibleOptionLink" href="#parameter-items/http_large_header_size_in_kb" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The maximum size of each buffer used for reading http client request header. This value indicates the maximum size allowed for each buffer. The allowed values for buffer size are 8, 16, 32 and 64.</div>
                                            <div>Applicable when action is &#x27;HTTP_HEADER&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/prefix"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-items/prefix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string to prepend to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_prefix_value`</div>
                                            <div>Applicable when action is one of [&#x27;EXTEND_HTTP_REQUEST_HEADER_VALUE&#x27;, &#x27;EXTEND_HTTP_RESPONSE_HEADER_VALUE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri"></div>
                    <b>redirect_uri</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri/host" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The valid domain name (hostname) or IP address to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the incoming HTTP request URI.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>Curly braces are valid in this property only to surround tokens, such as `{host}`</div>
                                            <div>Examples:</div>
                                            <div>*  **example.com** appears as `example.com` in the redirect URI.</div>
                                            <div>*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and the port is `8081` in the incoming HTTP request URI.</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri/path" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTP URI path to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{path}`, the service preserves the original path from the incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>The path string must begin with `/` if it does not begin with the `{path}` token.</div>
                                            <div>Examples:</div>
                                            <div>*  __/example/video/123__ appears as `/example/video/123` in the redirect URI.</div>
                                            <div>*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and `123` is the port in the incoming HTTP request URI.</div>
                                            <div>*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP request URI.</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri/port" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The communication port to use in the redirect URI.</div>
                                            <div>Valid values include integers from 1 to 65535.</div>
                                            <div>When this value is null, the service preserves the original port from the incoming HTTP request URI.</div>
                                            <div>Example: `8081`</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri/protocol" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTP protocol to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the incoming HTTP request URI. Allowed values are:</div>
                                            <div>*  HTTP *  HTTPS *  {protocol}</div>
                                            <div>`{protocol}` is the only valid token for this property. It can appear only once in the value string.</div>
                                            <div>Example: `HTTPS`</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/redirect_uri/query"></div>
                    <b>query</b>
                    <a class="ansibleOptionLink" href="#parameter-items/redirect_uri/query" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The query string to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{query}`, the service preserves the original query parameters from the incoming HTTP request URI.</div>
                                            <div>All `RedirectUri` tokens are valid for this property. You can use any token more than once.</div>
                                            <div>If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.</div>
                                            <div>You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand (&amp;) character. To omit all incoming query parameters from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>If the specified query string results in a redirect URI ending with `?` or `&amp;`, the last character is truncated. For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is `?lang=en&amp;{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system truncates the final ampersand (&amp;) because the incoming URI included no value to replace the {query} token.</div>
                                            <div>Examples: * **lang=en&amp;time_zone=PST** appears as `lang=en&amp;time_zone=PST` in the redirect URI.</div>
                                            <div>* **{query}** appears as `lang=en&amp;time_zone=PST` in the redirect URI if `lang=en&amp;time_zone=PST` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}` token renders as an empty string.</div>
                                            <div>* **lang=en&amp;{query}&amp;time_zone=PST** appears as `lang=en&amp;country=us&amp;time_zone=PST` in the redirect URI if `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, this value renders as `lang=en&amp;time_zone=PST`.</div>
                                            <div>*  **protocol={protocol}&amp;hostname={host}** appears as `protocol=http&amp;hostname=example.com` in the redirect URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request.</div>
                                            <div>*  **port={port}&amp;hostname={host}** appears as `port=8080&amp;hostname=example.com` in the redirect URI if the port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/response_code"></div>
                    <b>response_code</b>
                    <a class="ansibleOptionLink" href="#parameter-items/response_code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTP status code to return when the incoming request is redirected.</div>
                                            <div>The status line returned with the code is mapped from the standard HTTP specification. Valid response codes for redirection are:</div>
                                            <div>*  301 *  302 *  303 *  307 *  308</div>
                                            <div>The default value is `302` (Found).</div>
                                            <div>Example: `301`</div>
                                            <div>Applicable when action is &#x27;REDIRECT&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/status_code"></div>
                    <b>status_code</b>
                    <a class="ansibleOptionLink" href="#parameter-items/status_code" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The HTTP status code to return when the requested HTTP method is not in the list of allowed methods. The associated status line returned with the code is mapped from the standard HTTP specification. The default value is `405 (Method Not Allowed)`.</div>
                                            <div>Example: 403</div>
                                            <div>Applicable when action is &#x27;CONTROL_ACCESS_USING_HTTP_METHODS&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/suffix"></div>
                    <b>suffix</b>
                    <a class="ansibleOptionLink" href="#parameter-items/suffix" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A string to append to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_suffix_value`</div>
                                            <div>Applicable when action is one of [&#x27;EXTEND_HTTP_REQUEST_HEADER_VALUE&#x27;, &#x27;EXTEND_HTTP_RESPONSE_HEADER_VALUE&#x27;]</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-items/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A header value that conforms to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_value`</div>
                                            <div>Required when action is one of [&#x27;ADD_HTTP_RESPONSE_HEADER&#x27;, &#x27;ADD_HTTP_REQUEST_HEADER&#x27;]</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-load_balancer_id"></div>
                    <b>load_balancer_id</b>
                    <a class="ansibleOptionLink" href="#parameter-load_balancer_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the specified load balancer.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.</div>
                                            <div>Example: `example_rule_set`</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                            <div>The state of the RuleSet.</div>
                                            <div>Use <em>state=present</em> to create or update a RuleSet.</div>
                                            <div>Use <em>state=absent</em> to delete a RuleSet.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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
                                                                <td colspan="3">
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

    
    - name: Create rule_set
      oci_loadbalancer_rule_set:
        # required
        items:
        - # required
          value: value_example
          action: ADD_HTTP_REQUEST_HEADER
          header: header_example
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example

    - name: Update rule_set
      oci_loadbalancer_rule_set:
        # required
        items:
        - # required
          value: value_example
          action: ADD_HTTP_REQUEST_HEADER
          header: header_example
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example

    - name: Delete rule_set
      oci_loadbalancer_rule_set:
        # required
        load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
        name: name_example
        state: absent





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-rule_set"></div>
                    <b>rule_set</b>
                    <a class="ansibleOptionLink" href="#return-rule_set" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the RuleSet resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;items&#x27;: [{&#x27;action&#x27;: &#x27;ADD_HTTP_REQUEST_HEADER&#x27;, &#x27;allowed_methods&#x27;: [], &#x27;are_invalid_characters_allowed&#x27;: True, &#x27;conditions&#x27;: [{&#x27;attribute_name&#x27;: &#x27;SOURCE_IP_ADDRESS&#x27;, &#x27;attribute_value&#x27;: &#x27;attribute_value_example&#x27;, &#x27;operator&#x27;: &#x27;EXACT_MATCH&#x27;}], &#x27;description&#x27;: &#x27;description_example&#x27;, &#x27;header&#x27;: &#x27;header_example&#x27;, &#x27;http_large_header_size_in_kb&#x27;: 56, &#x27;prefix&#x27;: &#x27;prefix_example&#x27;, &#x27;redirect_uri&#x27;: {&#x27;host&#x27;: &#x27;host_example&#x27;, &#x27;path&#x27;: &#x27;path_example&#x27;, &#x27;port&#x27;: 56, &#x27;protocol&#x27;: &#x27;protocol_example&#x27;, &#x27;query&#x27;: &#x27;query_example&#x27;}, &#x27;response_code&#x27;: 56, &#x27;status_code&#x27;: 56, &#x27;suffix&#x27;: &#x27;suffix_example&#x27;, &#x27;value&#x27;: &#x27;value_example&#x27;}], &#x27;name&#x27;: &#x27;name_example&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of rules that compose the rule set.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ADD_HTTP_REQUEST_HEADER</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/allowed_methods"></div>
                    <b>allowed_methods</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/allowed_methods" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The list of HTTP methods allowed for this listener.</div>
                                            <div>By default, you can specify only the standard HTTP methods defined in the <a href='http://www.iana.org/assignments/http-methods/http-methods.xhtml'>HTTP Method Registry</a>. You can also see a list of supported standard HTTP methods in the Load Balancing service documentation at <a href='https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm'>Managing Rule Sets</a>.</div>
                                            <div>Your backend application must be able to handle the methods specified in this list.</div>
                                            <div>The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact <a href='http://support.oracle.com/'>My Oracle Support</a> to remove the restriction for your tenancy.</div>
                                            <div>Example: [&quot;GET&quot;, &quot;PUT&quot;, &quot;POST&quot;, &quot;PROPFIND&quot;]</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/are_invalid_characters_allowed"></div>
                    <b>are_invalid_characters_allowed</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/are_invalid_characters_allowed" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Indicates whether or not invalid characters in client header fields will be allowed. Valid names are composed of English letters, digits, hyphens and underscores. If &quot;true&quot;, invalid characters are allowed in the HTTP header. If &quot;false&quot;, invalid characters are not allowed in the HTTP header</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/conditions"></div>
                    <b>conditions</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/conditions" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/conditions/attribute_name"></div>
                    <b>attribute_name</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/conditions/attribute_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">SOURCE_IP_ADDRESS</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/conditions/attribute_value"></div>
                    <b>attribute_value</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/conditions/attribute_value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The path string that the redirection rule applies to.</div>
                                            <div>Example: `/example`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">attribute_value_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/conditions/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/conditions/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string that specifies how to compare the PathMatchCondition object&#x27;s `attributeValue` string to the incoming URI.</div>
                                            <div>*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string.</div>
                                            <div>*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best, longest match of the beginning portion of the incoming URI path.</div>
                                            <div>*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                            <div>*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue` string.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">EXACT_MATCH</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/description"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/description" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A brief description of the access control rule. Avoid entering confidential information.</div>
                                            <div>example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">description_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/header"></div>
                    <b>header</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/header" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A header name that conforms to RFC 7230.</div>
                                            <div>Example: `example_header_name`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">header_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/http_large_header_size_in_kb"></div>
                    <b>http_large_header_size_in_kb</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/http_large_header_size_in_kb" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The maximum size of each buffer used for reading http client request header. This value indicates the maximum size allowed for each buffer. The allowed values for buffer size are 8, 16, 32 and 64.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/prefix"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/prefix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string to prepend to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_prefix_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">prefix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri"></div>
                    <b>redirect_uri</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri/host"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri/host" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The valid domain name (hostname) or IP address to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the incoming HTTP request URI.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>Curly braces are valid in this property only to surround tokens, such as `{host}`</div>
                                            <div>Examples:</div>
                                            <div>*  **example.com** appears as `example.com` in the redirect URI.</div>
                                            <div>*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and the port is `8081` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">host_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri/path"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri/path" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP URI path to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{path}`, the service preserves the original path from the incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>All RedirectUri tokens are valid for this property. You can use any token more than once.</div>
                                            <div>The path string must begin with `/` if it does not begin with the `{path}` token.</div>
                                            <div>Examples:</div>
                                            <div>*  __/example/video/123__ appears as `/example/video/123` in the redirect URI.</div>
                                            <div>*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname in the incoming HTTP request URI.</div>
                                            <div>*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and `123` is the port in the incoming HTTP request URI.</div>
                                            <div>*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">path_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri/port"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri/port" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The communication port to use in the redirect URI.</div>
                                            <div>Valid values include integers from 1 to 65535.</div>
                                            <div>When this value is null, the service preserves the original port from the incoming HTTP request URI.</div>
                                            <div>Example: `8081`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri/protocol"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri/protocol" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP protocol to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the incoming HTTP request URI. Allowed values are:</div>
                                            <div>*  HTTP *  HTTPS *  {protocol}</div>
                                            <div>`{protocol}` is the only valid token for this property. It can appear only once in the value string.</div>
                                            <div>Example: `HTTPS`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">protocol_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/redirect_uri/query"></div>
                    <b>query</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/redirect_uri/query" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The query string to use in the redirect URI.</div>
                                            <div>When this value is null, not set, or set to `{query}`, the service preserves the original query parameters from the incoming HTTP request URI.</div>
                                            <div>All `RedirectUri` tokens are valid for this property. You can use any token more than once.</div>
                                            <div>If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.</div>
                                            <div>You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand (&amp;) character. To omit all incoming query parameters from the redirect URI, set this value to an empty string, &quot;&quot;.</div>
                                            <div>If the specified query string results in a redirect URI ending with `?` or `&amp;`, the last character is truncated. For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is `?lang=en&amp;{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system truncates the final ampersand (&amp;) because the incoming URI included no value to replace the {query} token.</div>
                                            <div>Examples: * **lang=en&amp;time_zone=PST** appears as `lang=en&amp;time_zone=PST` in the redirect URI.</div>
                                            <div>* **{query}** appears as `lang=en&amp;time_zone=PST` in the redirect URI if `lang=en&amp;time_zone=PST` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}` token renders as an empty string.</div>
                                            <div>* **lang=en&amp;{query}&amp;time_zone=PST** appears as `lang=en&amp;country=us&amp;time_zone=PST` in the redirect URI if `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query parameters, this value renders as `lang=en&amp;time_zone=PST`.</div>
                                            <div>*  **protocol={protocol}&amp;hostname={host}** appears as `protocol=http&amp;hostname=example.com` in the redirect URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request.</div>
                                            <div>*  **port={port}&amp;hostname={host}** appears as `port=8080&amp;hostname=example.com` in the redirect URI if the port is `8080` and the hostname is `example.com` in the incoming HTTP request URI.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">query_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/response_code"></div>
                    <b>response_code</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/response_code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP status code to return when the incoming request is redirected.</div>
                                            <div>The status line returned with the code is mapped from the standard HTTP specification. Valid response codes for redirection are:</div>
                                            <div>*  301 *  302 *  303 *  307 *  308</div>
                                            <div>The default value is `302` (Found).</div>
                                            <div>Example: `301`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/status_code"></div>
                    <b>status_code</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/status_code" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The HTTP status code to return when the requested HTTP method is not in the list of allowed methods. The associated status line returned with the code is mapped from the standard HTTP specification. The default value is `405 (Method Not Allowed)`.</div>
                                            <div>Example: 403</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/suffix"></div>
                    <b>suffix</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/suffix" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A string to append to the header value. The resulting header value must conform to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_suffix_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">suffix_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-rule_set/items/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/items/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A header value that conforms to RFC 7230. With the following exceptions: *  value cannot contain `$` *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid.</div>
                                            <div>Example: `example_value`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">value_example</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-rule_set/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-rule_set/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name for this set of rules. It must be unique and it cannot be changed. Avoid entering confidential information.</div>
                                            <div>Example: `example_rule_set`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
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

