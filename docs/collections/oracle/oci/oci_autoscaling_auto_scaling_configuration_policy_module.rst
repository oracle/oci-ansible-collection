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

.. _ansible_collections.oracle.oci.oci_autoscaling_auto_scaling_configuration_policy_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

oracle.oci.oci_autoscaling_auto_scaling_configuration_policy -- Manage an AutoScalingConfigurationPolicy resource in Oracle Cloud Infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `oracle.oci collection <https://galaxy.ansible.com/oracle/oci>`_ (version 4.33.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install oracle.oci`.

    To use it in a playbook, specify: :code:`oracle.oci.oci_autoscaling_auto_scaling_configuration_policy`.

.. version_added

.. versionadded:: 2.9.0 of oracle.oci

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module allows the user to update an AutoScalingConfigurationPolicy resource in Oracle Cloud Infrastructure


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
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-auto_scaling_configuration_id"></div>
                    <b>auto_scaling_configuration_id</b>
                    <a class="ansibleOptionLink" href="#parameter-auto_scaling_configuration_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The <a href='https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm'>OCID</a> of the autoscaling configuration.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-auto_scaling_policy_id"></div>
                    <b>auto_scaling_policy_id</b>
                    <a class="ansibleOptionLink" href="#parameter-auto_scaling_policy_id" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ID of the autoscaling policy.</div>
                                            <div>Required for update using <em>state=present</em> when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: id</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-capacity"></div>
                    <b>capacity</b>
                    <a class="ansibleOptionLink" href="#parameter-capacity" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The capacity requirements of the autoscaling policy.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-capacity/initial"></div>
                    <b>initial</b>
                    <a class="ansibleOptionLink" href="#parameter-capacity/initial" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the limits that you set.</div>
                                            <div>For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule that&#x27;s defined in the autoscaling policy.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-capacity/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#parameter-capacity/max" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed to increase to (scale out).</div>
                                            <div>For a schedule-based autoscaling policy, this value is not used.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-capacity/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#parameter-capacity/min" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed to decrease to (scale in).</div>
                                            <div>For a schedule-based autoscaling policy, this value is not used.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>Required for update when environment variable <code>OCI_USE_NAME_AS_IDENTIFIER</code> is set.</div>
                                            <div>This parameter is updatable when <code>OCI_USE_NAME_AS_IDENTIFIER</code> is not set.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-execution_schedule"></div>
                    <b>execution_schedule</b>
                    <a class="ansibleOptionLink" href="#parameter-execution_schedule" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The schedule for executing the autoscaling policy.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;scheduled&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-execution_schedule/expression"></div>
                    <b>expression</b>
                    <a class="ansibleOptionLink" href="#parameter-execution_schedule/expression" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A cron expression that represents the time at which to execute the autoscaling policy.</div>
                                            <div>Cron expressions have this format: `&lt;second&gt; &lt;minute&gt; &lt;hour&gt; &lt;day of month&gt; &lt;month&gt; &lt;day of week&gt; &lt;year&gt;`</div>
                                            <div>You can use special characters that are supported with the Quartz cron implementation.</div>
                                            <div>You must specify `0` as the value for seconds.</div>
                                            <div>Example: `0 15 10 ? * *`</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-execution_schedule/timezone"></div>
                    <b>timezone</b>
                    <a class="ansibleOptionLink" href="#parameter-execution_schedule/timezone" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>UTC</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The time zone for the execution schedule.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-execution_schedule/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-execution_schedule/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>cron</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of execution schedule.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-is_enabled" title="Permalink to this option"></a>
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
                                            <div>Whether the autoscaling policy is enabled.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#parameter-policy_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>threshold</li>
                                                                                                                                                                                                <li>scheduled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Indicates the type of autoscaling policy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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
                                                                <td colspan="4">
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
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-resource_action"></div>
                    <b>resource_action</b>
                    <a class="ansibleOptionLink" href="#parameter-resource_action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;scheduled&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-resource_action/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-resource_action/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>STOP</li>
                                                                                                                                                                                                <li>START</li>
                                                                                                                                                                                                <li>SOFTRESET</li>
                                                                                                                                                                                                <li>RESET</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-resource_action/action_type"></div>
                    <b>action_type</b>
                    <a class="ansibleOptionLink" href="#parameter-resource_action/action_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>power</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of resource action.</div>
                                            <div>This parameter is updatable.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-rules" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/action" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/action/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/action/type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CHANGE_COUNT_BY</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The type of action to take.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/action/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/action/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of instances), provide a negative value.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/display_name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Applicable when policy_type is &#x27;threshold&#x27;</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-rules/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/metric" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/metric/metric_type" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>CPU_UTILIZATION</li>
                                                                                                                                                                                                <li>MEMORY_UTILIZATION</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-rules/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/metric/threshold" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rules/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/metric/threshold/operator" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>GT</li>
                                                                                                                                                                                                <li>GTE</li>
                                                                                                                                                                                                <li>LT</li>
                                                                                                                                                                                                <li>LTE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).</div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-rules/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-rules/metric/threshold/value" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div></div>
                                            <div>This parameter is updatable.</div>
                                            <div>Required when policy_type is &#x27;threshold&#x27;</div>
                                                        </td>
            </tr>
                    
                    
                    
                                <tr>
                                                                <td colspan="4">
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
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The state of the AutoScalingConfigurationPolicy.</div>
                                            <div>Use <em>state=present</em> to update an existing an AutoScalingConfigurationPolicy.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="4">
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

    
    - name: Update auto_scaling_configuration_policy with policy_type = threshold
      oci_autoscaling_auto_scaling_configuration_policy:
        # required
        policy_type: threshold

        # optional
        rules:
        - # required
          action:
            # required
            type: CHANGE_COUNT_BY
            value: 56
          metric:
            # required
            metric_type: CPU_UTILIZATION
            threshold:
              # required
              operator: GT
              value: 56

          # optional
          display_name: display_name_example
        display_name: display_name_example
        capacity:
          # optional
          max: 56
          min: 56
          initial: 56
        is_enabled: true

    - name: Update auto_scaling_configuration_policy with policy_type = scheduled
      oci_autoscaling_auto_scaling_configuration_policy:
        # required
        policy_type: scheduled

        # optional
        display_name: display_name_example
        capacity:
          # optional
          max: 56
          min: 56
          initial: 56
        is_enabled: true
        execution_schedule:
          # required
          type: cron
          timezone: UTC
          expression: expression_example
        resource_action:
          # required
          action_type: power
          action: STOP

    - name: Update auto_scaling_configuration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with policy_type = threshold
      oci_autoscaling_auto_scaling_configuration_policy:
        # required
        policy_type: threshold

        # optional
        rules:
        - # required
          action:
            # required
            type: CHANGE_COUNT_BY
            value: 56
          metric:
            # required
            metric_type: CPU_UTILIZATION
            threshold:
              # required
              operator: GT
              value: 56

          # optional
          display_name: display_name_example
        display_name: display_name_example
        capacity:
          # optional
          max: 56
          min: 56
          initial: 56
        is_enabled: true

    - name: Update auto_scaling_configuration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with policy_type = scheduled
      oci_autoscaling_auto_scaling_configuration_policy:
        # required
        policy_type: scheduled

        # optional
        display_name: display_name_example
        capacity:
          # optional
          max: 56
          min: 56
          initial: 56
        is_enabled: true
        execution_schedule:
          # required
          type: cron
          timezone: UTC
          expression: expression_example
        resource_action:
          # required
          action_type: power
          action: STOP





.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy"></div>
                    <b>auto_scaling_configuration_policy</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Details of the AutoScalingConfigurationPolicy resource acted upon by the current operation</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;capacity&#x27;: {&#x27;initial&#x27;: 56, &#x27;max&#x27;: 56, &#x27;min&#x27;: 56}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;execution_schedule&#x27;: {&#x27;expression&#x27;: &#x27;expression_example&#x27;, &#x27;timezone&#x27;: &#x27;UTC&#x27;, &#x27;type&#x27;: &#x27;cron&#x27;}, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;is_enabled&#x27;: True, &#x27;policy_type&#x27;: &#x27;scheduled&#x27;, &#x27;resource_action&#x27;: {&#x27;action&#x27;: &#x27;STOP&#x27;, &#x27;action_type&#x27;: &#x27;power&#x27;}, &#x27;rules&#x27;: [{&#x27;action&#x27;: {&#x27;type&#x27;: &#x27;CHANGE_COUNT_BY&#x27;, &#x27;value&#x27;: 56}, &#x27;display_name&#x27;: &#x27;display_name_example&#x27;, &#x27;id&#x27;: &#x27;ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx&#x27;, &#x27;metric&#x27;: {&#x27;metric_type&#x27;: &#x27;CPU_UTILIZATION&#x27;, &#x27;threshold&#x27;: {&#x27;operator&#x27;: &#x27;GT&#x27;, &#x27;value&#x27;: 56}}}], &#x27;time_created&#x27;: &#x27;2013-10-20T19:20:30+01:00&#x27;}</div>
                                    </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/capacity"></div>
                    <b>capacity</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/capacity" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The capacity requirements of the autoscaling policy.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/capacity/initial"></div>
                    <b>initial</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/capacity/initial" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this initial number to a number that is based on the limits that you set.</div>
                                            <div>For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule that&#x27;s defined in the autoscaling policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/capacity/max"></div>
                    <b>max</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/capacity/max" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed to increase to (scale out).</div>
                                            <div>For a schedule-based autoscaling policy, this value is not used.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/capacity/min"></div>
                    <b>min</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/capacity/min" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed to decrease to (scale in).</div>
                                            <div>For a schedule-based autoscaling policy, this value is not used.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/execution_schedule"></div>
                    <b>execution_schedule</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/execution_schedule" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">complex</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The schedule for executing the autoscaling policy.</div>
                                        <br/>
                                                        </td>
            </tr>
                                        <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/execution_schedule/expression"></div>
                    <b>expression</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/execution_schedule/expression" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A cron expression that represents the time at which to execute the autoscaling policy.</div>
                                            <div>Cron expressions have this format: `&lt;second&gt; &lt;minute&gt; &lt;hour&gt; &lt;day of month&gt; &lt;month&gt; &lt;day of week&gt; &lt;year&gt;`</div>
                                            <div>You can use special characters that are supported with the Quartz cron implementation.</div>
                                            <div>You must specify `0` as the value for seconds.</div>
                                            <div>Example: `0 15 10 ? * *`</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">expression_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/execution_schedule/timezone"></div>
                    <b>timezone</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/execution_schedule/timezone" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The time zone for the execution schedule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">UTC</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/execution_schedule/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/execution_schedule/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of execution schedule.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">cron</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The ID of the autoscaling policy that is assigned after creation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/is_enabled"></div>
                    <b>is_enabled</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/is_enabled" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>Whether the autoscaling policy is enabled.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/policy_type"></div>
                    <b>policy_type</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/policy_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of autoscaling policy.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">scheduled</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/resource_action"></div>
                    <b>resource_action</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/resource_action" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/resource_action/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/resource_action/action" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">STOP</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/resource_action/action_type"></div>
                    <b>action_type</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/resource_action/action_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of resource action.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">power</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules" title="Permalink to this return value"></a>
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
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/action"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/action" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/action/type"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/action/type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The type of action to take.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CHANGE_COUNT_BY</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/action/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/action/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of instances), provide a negative value.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/display_name"></div>
                    <b>display_name</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/display_name" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>A user-friendly name. Does not have to be unique, and it&#x27;s changeable. Avoid entering confidential information.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">display_name_example</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/id"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/id" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>ID of the condition that is assigned after creation.</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/metric"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/metric" title="Permalink to this return value"></a>
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
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/metric/metric_type"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/metric/metric_type" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">CPU_UTILIZATION</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/metric/threshold"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/metric/threshold" title="Permalink to this return value"></a>
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
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/metric/threshold/operator"></div>
                    <b>operator</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/metric/threshold/operator" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The comparison operator to use. Options are greater than (`GT`), greater than or equal to (`GTE`), less than (`LT`), and less than or equal to (`LTE`).</div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">GT</div>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/rules/metric/threshold/value"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/rules/metric/threshold/value" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">integer</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div></div>
                                        <br/>
                                                                <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">56</div>
                                    </td>
            </tr>
                    
                    
                    
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="return-auto_scaling_configuration_policy/time_created"></div>
                    <b>time_created</b>
                    <a class="ansibleOptionLink" href="#return-auto_scaling_configuration_policy/time_created" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                                          </div>
                                    </td>
                <td>on success</td>
                <td>
                                            <div>The date and time the autoscaling configuration was created, in the format defined by RFC3339.</div>
                                            <div>Example: `2016-08-25T21:10:29.600Z`</div>
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

