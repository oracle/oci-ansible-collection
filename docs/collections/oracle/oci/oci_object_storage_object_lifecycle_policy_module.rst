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

.. _ansible_collections.oracle.oci.oci_object_storage_object_lifecycle_policy_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_object_storage_object_lifecycle_policy -- Manage an ObjectLifecyclePolicy resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 5.5.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_object_storage_object_lifecycle_policy`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to update and delete an ObjectLifecyclePolicy resource in Oracle Cloud Infrastructure


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
                    <div class="ansibleOptionAnchor" id="parameter-bucket_name"></div>
                    <b>bucket_name</b>
                    <a class="ansibleOptionLink" href="#parameter-bucket_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`</div>
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
                                            <div>The bucket&#x27;s set of lifecycle policy rules.</div>
                                            <div>This parameter is updatable.</div>
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
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The action of the object lifecycle policy rule. Rules using the action &#x27;ARCHIVE&#x27; move objects from Standard and InfrequentAccess storage tiers into the <a href='https://docs.cloud.oracle.com/Content/Archive/Concepts/archivestorageoverview.htm'>Archive storage tier</a>. Rules using the action &#x27;INFREQUENT_ACCESS&#x27; move objects from Standard storage tier into the Infrequent Access Storage tier. Objects that are already in InfrequentAccess tier or in Archive tier are left untouched. Rules using the action &#x27;DELETE&#x27; permanently delete objects from buckets. Rules using &#x27;ABORT&#x27; abort the uncommitted multipart-uploads and permanently delete their parts from buckets.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-items/is_enabled" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>A Boolean that determines whether this rule is currently enabled.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-items/name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the lifecycle rule to be applied.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_name_filter"></div>
                    <b>object_name_filter</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_name_filter" title="Permalink to this option"></a>
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
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_name_filter/exclusion_patterns"></div>
                    <b>exclusion_patterns</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_name_filter/exclusion_patterns" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters.</div>
                                            <div>The special pattern characters have the following meanings:</div>
                                            <div>\           Escapes the following character *           Matches any string of characters. ?           Matches any single character . [...]       Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a &#x27;-&#x27; in the range, make it the first or last character.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_name_filter/inclusion_patterns"></div>
                    <b>inclusion_patterns</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_name_filter/inclusion_patterns" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of glob patterns to match the object names to include. An empty array includes all objects in the bucket. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters.</div>
                                            <div>The special pattern characters have the following meanings:</div>
                                            <div>\           Escapes the following character *           Matches any string of characters. ?           Matches any single character . [...]       Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a &#x27;-&#x27; in the range, make it the first or last character.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-items/object_name_filter/inclusion_prefixes"></div>
                    <b>inclusion_prefixes</b>
                    <a class="ansibleOptionLink" href="#parameter-items/object_name_filter/inclusion_prefixes" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>An array of object name prefixes that the rule will apply to. An empty array means to include all objects.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/target"></div>
                    <b>target</b>
                    <a class="ansibleOptionLink" href="#parameter-items/target" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The target of the object lifecycle policy rule. The values of target can be either &quot;objects&quot;, &quot;multipart-uploads&quot; or &quot;previous-object-versions&quot;. This field when declared as &quot;objects&quot; is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for objects. This field when declared as &quot;previous-object-versions&quot; is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for previous versions of existing objects. This field when declared as &quot;multipart-uploads&quot; is used to specify the ABORT (only) rule for uncommitted multipart-uploads.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/time_amount"></div>
                    <b>time_amount</b>
                    <a class="ansibleOptionLink" href="#parameter-items/time_amount" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation to each object&#x27;s Last-Modified time.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-items/time_unit"></div>
                    <b>time_unit</b>
                    <a class="ansibleOptionLink" href="#parameter-items/time_unit" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>DAYS</li>
                                                                                                                                                                                                <li>YEARS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC. Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-namespace_name"></div>
                    <b>namespace_name</b>
                    <a class="ansibleOptionLink" href="#parameter-namespace_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The Object Storage namespace used for the request.</div>
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
                                            <div>The state of the ObjectLifecyclePolicy.</div>
                                            <div>Use <em>state=present</em> to update an existing an ObjectLifecyclePolicy.</div>
                                            <div>Use <em>state=absent</em> to delete an ObjectLifecyclePolicy.</div>
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

    
    - name: Update object_lifecycle_policy
      oci_object_storage_object_lifecycle_policy:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example

        # optional
        items:
        - # required
          name: name_example
          action: action_example
          time_amount: 56
          time_unit: DAYS
          is_enabled: true

          # optional
          target: target_example
          object_name_filter:
            # optional
            inclusion_prefixes: [ "inclusion_prefixes_example" ]
            inclusion_patterns: [ "inclusion_patterns_example" ]
            exclusion_patterns: [ "exclusion_patterns_example" ]

    - name: Delete object_lifecycle_policy
      oci_object_storage_object_lifecycle_policy:
        # required
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
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
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy"></div>
                    <b>object_lifecycle_policy</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the ObjectLifecyclePolicy resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;items&#x27;: [{&#x27;action&#x27;: &#x27;action_example&#x27;, &#x27;is_enabled&#x27;: True, &#x27;name&#x27;: &#x27;name_example&#x27;, &#x27;object_name_filter&#x27;: {&#x27;exclusion_patterns&#x27;: [], &#x27;inclusion_patterns&#x27;: [], &#x27;inclusion_prefixes&#x27;: []}, &#x27;target&#x27;: &#x27;target_example&#x27;, &#x27;time_amount&#x27;: 56, &#x27;time_unit&#x27;: &#x27;DAYS&#x27;}], &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items"></div>
                    <b>items</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The live lifecycle policy on the bucket.</div>
                                            <div>For an example of this value, see the <a href='https://docs.cloud.oracle.com/iaas/api/#/en/objectstorage/20160918/ObjectLifecyclePolicy/PutObjectLifecyclePolicy'>PutObjectLifecyclePolicy API documentation</a>.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The action of the object lifecycle policy rule. Rules using the action &#x27;ARCHIVE&#x27; move objects from Standard and InfrequentAccess storage tiers into the <a href='https://docs.cloud.oracle.com/Content/Archive/Concepts/archivestorageoverview.htm'>Archive storage tier</a>. Rules using the action &#x27;INFREQUENT_ACCESS&#x27; move objects from Standard storage tier into the Infrequent Access Storage tier. Objects that are already in InfrequentAccess tier or in Archive tier are left untouched. Rules using the action &#x27;DELETE&#x27; permanently delete objects from buckets. Rules using &#x27;ABORT&#x27; abort the uncommitted multipart-uploads and permanently delete their parts from buckets.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">action_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A Boolean that determines whether this rule is currently enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The name of the lifecycle rule to be applied.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/object_name_filter"></div>
                    <b>object_name_filter</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/object_name_filter" title="Permalink to this return value"></a>
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
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/object_name_filter/exclusion_patterns"></div>
                    <b>exclusion_patterns</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/object_name_filter/exclusion_patterns" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of glob patterns to match the object names to exclude. An empty array is ignored. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters.</div>
                                            <div>The special pattern characters have the following meanings:</div>
                                            <div>\           Escapes the following character *           Matches any string of characters. ?           Matches any single character . [...]       Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a &#x27;-&#x27; in the range, make it the first or last character.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/object_name_filter/inclusion_patterns"></div>
                    <b>inclusion_patterns</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/object_name_filter/inclusion_patterns" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of glob patterns to match the object names to include. An empty array includes all objects in the bucket. Exclusion patterns take precedence over inclusion patterns. A Glob pattern is a sequence of characters to match text. Any character that appears in the pattern, other than the special pattern characters described below, matches itself. Glob patterns must be between 1 and 1024 characters.</div>
                                            <div>The special pattern characters have the following meanings:</div>
                                            <div>\           Escapes the following character *           Matches any string of characters. ?           Matches any single character . [...]       Matches a group of characters. A group of characters can be: A set of characters, for example: [Zafg9@]. This matches any character in the brackets. A range of characters, for example: [a-z]. This matches any character in the range. [a-f] is equivalent to [abcdef]. For character ranges only the CHARACTER-CHARACTER pattern is supported. [ab-yz] is not valid [a-mn-z] is not valid Character ranges can not start with ^ or : To include a &#x27;-&#x27; in the range, make it the first or last character.</div>
                                        <br/>
                                                        </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/object_name_filter/inclusion_prefixes"></div>
                    <b>inclusion_prefixes</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/object_name_filter/inclusion_prefixes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>An array of object name prefixes that the rule will apply to. An empty array means to include all objects.</div>
                                        <br/>
                                                        </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/target"></div>
                    <b>target</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/target" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The target of the object lifecycle policy rule. The values of target can be either &quot;objects&quot;, &quot;multipart-uploads&quot; or &quot;previous-object-versions&quot;. This field when declared as &quot;objects&quot; is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for objects. This field when declared as &quot;previous-object-versions&quot; is used to specify ARCHIVE, INFREQUENT_ACCESS or DELETE rule for previous versions of existing objects. This field when declared as &quot;multipart-uploads&quot; is used to specify the ABORT (only) rule for uncommitted multipart-uploads.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">target_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/time_amount"></div>
                    <b>time_amount</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/time_amount" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the timeUnit parameter, and is calculated in relation to each object&#x27;s Last-Modified time.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/items/time_unit"></div>
                    <b>time_unit</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/items/time_unit" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC. Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">DAYS</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-object_lifecycle_policy/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-object_lifecycle_policy/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the object lifecycle policy was created, as described in <a href='https://tools.ietf.org/html/rfc3339'>RFC 3339</a>.</div>
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

